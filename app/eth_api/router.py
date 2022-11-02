from . import get_web3 as gw3
from . import crud
from .schemas import EthBlock, BlockNumber
from app.database import get_db
from fastapi import APIRouter, Depends
from functools import lru_cache
from sqlalchemy.orm import Session


eth_router = APIRouter(
    prefix='/eth'
)


@eth_router.get('/tests')
def get_test():
    return {"message": "this is only a tests"}


@lru_cache()
@eth_router.get('/get_block/{block_num}')
def get_block(block_num=0, db: Session = Depends(get_db)):
    block = crud.read_block(db=db, block_num=block_num)
    if block is None:
        block = EthBlock(**get_web3_block(block_num))
    return block


@eth_router.get('/get_latest_block_num')
def get_latest_block_num():
    latest_num = gw3.BlockChainRequester().get_block_num()
    block_num = BlockNumber(block_number=latest_num)
    return block_num


@eth_router.post('/add_block/{block_num}', status_code=201)
def add_block(block_num=0, db: Session = Depends(get_db)):
    new_block = EthBlock(**get_web3_block(block_num))
    block_add = crud.create_block(db=db, eth_block=new_block)
    return block_add


def get_web3_block(block_num=0):
    bc = gw3.BlockChainRequester()
    block = bc.get_block(block_num)
    return block
