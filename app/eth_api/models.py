from app.database import Base
from sqlalchemy import Column, BigInteger, Integer, String


class EthBlock(Base):
    __tablename__ = "eth_block"
    __table_args__ = {'extend_existing': True}

    number = Column(Integer, primary_key=True, autoincrement=False)
    hash = Column(String(100), nullable=False)
    parent_hash = Column(String(100), nullable=False)
    nonce = Column(Integer, nullable=False)

