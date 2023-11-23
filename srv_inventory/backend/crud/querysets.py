from sqlalchemy.orm import Session
from backend.models.product import Product
from backend.models.category import Category


def create_init_category(db: Session, category: Category):
    db_category = Category(
        name=category.name
    )
    db.add(db_category)
    db.commit()
    db.refresh(db_category)

    return db_category


def create_init_product(db: Session, product: Product):
    db_product = Product(
        name=product.name,
        amount=product.amount,
        price=product.price,
        category_id=product.category_id
    )
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_product_by_id(db: Session, product_id: int) -> Product:
    return db.query(Product).filter(Product.id == product_id).first()
