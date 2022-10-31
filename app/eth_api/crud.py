from sqlalchemy.orm import Session
from . import schemas
from . import models
from web3 import Web3


def create_block(db: Session, eth_block: schemas.EthBlock):
    new_block = models.EthBlock(**eth_block.dict())
    check_block = db.get(models.EthBlock, eth_block.number)
    if check_block is None:
        db.add(new_block)
        db.commit()
        db.refresh(new_block)
        return new_block
    else:
        return {"message": "block already exists in db"}


def read(db: Session, block_num: int):
    query_block = db.get(models.EthBlock, block_num)
    return query_block


def update(db: Session, block_num: int):
        pass


def delete():
    pass


def format_block(block):
    new_block = schemas.EthBlock(
        number=Web3.toInt(block["number"]),
        hash=Web3.toInt(block["hash"]),
        parent_hash=Web3.toInt(block["parentHash"]),
        nonce=Web3.toInt(block["nonce"])
    )
    return new_block
