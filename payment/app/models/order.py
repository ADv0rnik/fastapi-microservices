from db.base_class import Base
from sqlalchemy import Column, Integer, String, Float


class Order(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    product_id = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)
    total = Column(Float, nullable=False)

