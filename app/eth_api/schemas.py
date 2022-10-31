from pydantic import BaseModel


class EthBlock(BaseModel):
    number: int
    hash: str
    parent_hash: str
    nonce: int
