from app.eth_api import models
from app.database import engine
from eth_api import create_app
import uvicorn
from eth_api.get_web3 import BlockChainRequester
import pprint as pp

app = create_app()
models.Base.metadata.create_all(bind=engine)

test_w3 = BlockChainRequester()
lb = test_w3.get_latest_block()

print(f"latest hash = {test_w3.get_latest_block_hash()}")

if __name__ == "__main__":
    uvicorn.run("app.main:app", port=5000, reload=True)
