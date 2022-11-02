from app.eth_api import models
from app.database import engine
from app.eth_api import create_app
import uvicorn
from app.eth_api import get_web3 as gw3

app = create_app()
models.Base.metadata.create_all(bind=engine)

# --------------------
# testing stuff
# --------------------
# test = gw3.BlockChainRequester()

if __name__ == "__main__":
    uvicorn.run("app.main:app", port=5000, reload=True)
