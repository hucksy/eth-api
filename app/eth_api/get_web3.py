from app.config import get_env_configs
from web3 import Web3
import json


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

    def get_block(self, block_num: int) -> json:
        block = self.w3.eth.get_block(Web3.toHex(int(block_num)))
        block_json = json.loads(Web3.toJSON(block))
        return block_json

    def get_block_num(self) -> int:
        return self.w3.eth.block_number
