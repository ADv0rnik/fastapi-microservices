from db.base_class import Base
from sqlalchemy import Column, Integer, String, Float


class Product(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    amount = Column(Integer, default=0)
    price = Column(Float, default=0.0)


