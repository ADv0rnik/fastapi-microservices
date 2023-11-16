from pydantic import BaseModel


class ProductBaseModel(BaseModel):
    name: str
    amount: int
    price: float


class ProductCreateModel(ProductBaseModel):
    pass


class ProductModel(ProductBaseModel):
    id: int

    class Config:
        orm_mode = True
