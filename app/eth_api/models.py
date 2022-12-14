from app.database import Base
from sqlalchemy import Column, BigInteger, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY


class EthBlock(Base):
    __tablename__ = "eth_block"
    __table_args__ = {'extend_existing': True}

    number = Column(Integer, primary_key=True, autoincrement=False)
    hash = Column(String, nullable=False)
    parent_hash = Column(String, nullable=False)
    nonce = Column(String, nullable=False)
    base_fee_per_gas = Column(BigInteger, nullable=False)
    difficulty = Column(Integer, nullable=False)
    extra_data = Column(String, nullable=True)
    gas_limit = Column(BigInteger, nullable=False)
    gas_used = Column(BigInteger, nullable=False)
    logs_bloom = Column(String)
    miner = Column(String, nullable=False)
    mix_hash = Column(String, nullable=False)
    receipts_root = Column(String, nullable=False)
    sha3_uncles = Column(String, nullable=False)
    size = Column(Integer, nullable=False)
    state_root = Column(String, nullable=False)
    timestamp = Column(BigInteger, nullable=False)
    total_difficulty = Column(String, nullable=False)
    transactions = Column(ARRAY(String), nullable=False)
    transactions_root = Column(String, nullable=False)
    uncles = Column(String, nullable=False)

