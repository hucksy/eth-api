from app.config import get_env_configs
from web3 import Web3
from . import schemas
import json
# from web3 import EthereumTesterProvider


class BlockChainRequester:
    def __init__(self):
        self.w3 = None
        self.connect()

    def connect(self):
        self.w3 = Web3(Web3.HTTPProvider(get_env_configs().INFURA_ENDPOINT))
        # self.w3 = Web3(EthereumTesterProvider())
        try:
            assert (self.w3.isConnected())
        except Exception as e:
            print(e)

    def get_block(self):
        latest_block = self.w3.eth.get_block('latest')
        lb_json = json.loads(Web3.toJSON(latest_block))
        return lb_json


def format_block(block):
    new_block = schemas.EthBlock(
        number=Web3.toInt(block["number"]),
        hash=str(Web3.toInt(block["hash"])),
        parent_hash=str(Web3.toInt(block["parentHash"])),
        nonce=Web3.toInt(block["nonce"])
    )
    return new_block
