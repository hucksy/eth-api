from . import get_web3 as gw3
from . import crud
from . import schemas
from app.database import get_db
from fastapi import APIRouter, Depends, Response
from sqlalchemy.orm import Session
from web3 import Web3

eth_router = APIRouter(
    prefix='/eth'
)


@eth_router.get('/tests')
async def get_test():
    return {"message": "this is only a tests"}


# TO-DO: pull this from db instead
@eth_router.get('/latest_block')
async def get_latest_block():
    latest_block = Web3.toJSON(request_block())
    return {"latest_block": latest_block}


@eth_router.post('/add_block')
async def add_latest_block(db: Session = Depends(get_db)):
    latest_block = gw3.format_block(request_block())
    add_block = crud.create_block(db=db, eth_block=latest_block)
    return add_block


# TO-DO paramterize inputs
def request_block():
    bc = gw3.BlockChainRequester()
    block = bc.get_latest_block()
    return block
