from .schemas import ProductModel
from .router import router
from fastapi import APIRouter, Response
from starlette.requests import Request

product_router = APIRouter(prefix="/products")


@router(
    method=product_router.get,
    path="/{product_id}",
    response_model=ProductModel
)
async def get_product_by_id(
        request: Request, response: Response, product_id: int
):
    pass
