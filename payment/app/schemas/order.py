from typing import Optional

from pydantic import BaseModel


class OrderBaseModel(BaseModel):
    product_id: int
    comment: Optional[str]
    total: float


class OrderCreateModel(OrderBaseModel):
    pass


class OrderModel(OrderBaseModel):
    id: int

    class Config:
        orm_mode = True
