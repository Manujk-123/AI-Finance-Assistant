from sqlalchemy import Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class Transaction(Base):
    __tablename__ = "transactions"
    id = Column(Integer, primary_key=True, index=True)
    text = Column(String, nullable=True)
    amount = Column(Float, default=0.0)
    txn_type = Column(String, nullable=True)
    method = Column(String, nullable=True)
    category = Column(String, nullable=True)
    received_at = Column(DateTime, default=datetime.datetime.utcnow)
