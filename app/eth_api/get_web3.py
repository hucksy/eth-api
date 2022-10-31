from app.config import get_env_configs
from web3 import Web3
from . import schemas
# from web3 import EthereumTesterProvider


class BlockChainRequester:
    def __init__(self):
        self.connect()
        self.w3 = None

    async def connect(self):
        self.w3 = Web3(Web3.HTTPProvider(get_env_configs().INFURA_ENDPOINT))
        # self.w3 = Web3(EthereumTesterProvider())
        try:
            assert (self.w3.isConnected())
        except Exception as e:
            print(e)

    async def get_latest_block(self):
        latest_block = self.w3.eth.get_block('latest')
        return latest_block

    async def get_latest_block_hash(self):
        latest_block = self.w3.eth.get_block('latest')
        latest_hash_binary = dict(latest_block).get('hash')
        return self.w3.toInt(latest_hash_binary)


def format_block(block):
    new_block = schemas.EthBlock(
        number=Web3.toInt(block["number"]),
        hash=str(Web3.toInt(block["hash"])),
        parent_hash=str(Web3.toInt(block["parentHash"])),
        nonce=Web3.toInt(block["nonce"])
    )
    return new_block
