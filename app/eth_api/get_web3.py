from app.config import get_env_configs
from web3 import Web3
from web3 import EthereumTesterProvider


class BlockChainRequester:
    def __init__(self):
        # self.w3 = Web3(Web3.HTTPProvider(get_env_configs().INFURA_ENDPOINT))
        self.w3 = Web3(EthereumTesterProvider())
        self.check_connection()

    def check_connection(self):
        try:
            assert (self.w3.isConnected())
        except Exception as e:
            print(e)

    def say_hello(self):
        return f"Hi i am a {type(self)}"

    def get_latest_block(self, return_type=None):
        latest_block = self.w3.eth.get_block('latest')
        if return_type == 'json':
            return Web3.toJSON(latest_block)
        else:
            return dict(latest_block)

    def get_latest_block_hash(self):
        latest_block = self.w3.eth.get_block('latest')
        latest_hash_binary = dict(latest_block).get('hash')
        print(f"latest_hash_binary = {latest_hash_binary}")
        print(f"in get_latest_block_hash, hash = {self.w3.toInt(primitive=latest_hash_binary)}")
        # l_hash = self.w3.toText(hexstr=latest_block['hash'])
