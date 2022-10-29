from fastapi import APIRouter
from .get_web3 import BlockChainRequester

eth_router = APIRouter(
    prefix='/eth'
)


@eth_router.get('/test')
async def get_test():
    return {"message": "this is only a test"}


@eth_router.get('/latest_block')
async def get_latest_block():
    bc = BlockChainRequester()
    latest_block = bc.get_latest_block(return_type='json')
    return {"latest_block": latest_block}
