from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from backend.db.base_class import Base
from .category import Category


class Product(Base):
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(50), nullable=False)
    amount = Column(Integer, default=0)
    price = Column(Float, default=0.0)
    category_id = Column(Integer, ForeignKey('category.id'), nullable=False)

    category = relationship("Category", back_populates="product")
