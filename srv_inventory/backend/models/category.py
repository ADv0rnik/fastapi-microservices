from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from backend.db.base_class import Base


class Category(Base):
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True, comment="Category name")

    product = relationship("Product", back_populates="category")
