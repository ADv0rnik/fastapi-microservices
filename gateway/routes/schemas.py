from pydantic import BaseModel


class ProductBaseModel(BaseModel):
    name: str
    amount: int
    price: float
    category_id: int


class ProductCreateModel(ProductBaseModel):
    pass


class ProductUpdateModel(ProductBaseModel):
    pass


class ProductModel(ProductBaseModel):
    id: int

    class Config:
        orm_mode = True


class CategoryBaseModel(BaseModel):
    name: str


class CategoryCreateModel(CategoryBaseModel):
    pass


class CategoryModel(CategoryBaseModel):
    id: int

    class Config:
        orm_mode = True
