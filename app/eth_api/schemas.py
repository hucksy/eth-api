from pydantic import BaseModel, Field
from typing import List, Optional


class TestSchema(BaseModel):
    num: int
    name: str


class EthBlock(BaseModel):
    number: int
    hash: str
    parent_hash: str = Field(alias='parentHash')
    nonce: str
    base_fee_per_gas: int = Field(alias='baseFeePerGas')
    difficulty: int
    extra_data: str = Field(alias='extraData')
    gas_limit: int = Field(alias='gasLimit')
    gas_used: int = Field(alias='gasUsed')
    logs_bloom: str = Field(alias='logsBloom')
    miner: str
    mix_hash: str = Field(alias='mixHash')
    receipts_root: str = Field(alias='receiptsRoot')
    sha3_uncles: str = Field(alias='sha3Uncles')
    size: str
    state_root: str = Field(alias='stateRoot')
    timestamp: int
    total_difficulty: int = Field(alias='totalDifficulty')
    transactions: List[str]
    transactions_root: str = Field(alias='transactionsRoot')
    uncles: Optional[List[str]]
