from sqlalchemy.orm import Session
from typing import Union
from . import schemas
from . import models


def create_block(db: Session, eth_block: schemas.EthBlock) -> Union[models.EthBlock, dict]:
    new_block = models.EthBlock(**eth_block.dict())
    if unique_block(db, eth_block.number):
        db.add(new_block)
        db.commit()
        db.refresh(new_block)
        return new_block
    else:
        return {"message": "block already exists in db"}


def unique_block(db, block_number) -> bool:
    return read_block(db, block_number) is None


def read_block(db: Session, block_num: int):
    query_block = db.get(models.EthBlock, block_num)
    return query_block


def update_block(db: Session, block_num: int):
    pass


def delete_block():
    pass
