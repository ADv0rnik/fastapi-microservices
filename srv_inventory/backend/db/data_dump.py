from backend.core.config import INIT_PRODUCT, INIT_CATEGORY
from backend.crud.querysets import create_init_category, create_init_product
from sqlalchemy.orm import Session
from backend.schemas.schemas import CategoryCreateModel, ProductCreateModel


def init_db(db: Session):
    create_category(db)
    create_product(db)


def create_category(db: Session):
    if category := INIT_CATEGORY:
        db_category = CategoryCreateModel(
            name=category.get("name")
        )

        create_init_category(db, db_category)


def create_product(db: Session):
    products = INIT_PRODUCT

    for product in products:
        db_product = ProductCreateModel(
            name=product.get("name"),
            amount=product.get("amount"),
            price=product.get("price"),
            category_id=product.get("category_id")
        )

        try:
            create_init_product(db, db_product)
        except Exception as error:
            print(error)
