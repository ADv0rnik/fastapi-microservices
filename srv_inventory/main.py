import json
import uvicorn

from fastapi import FastAPI, Depends, HTTPException
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response
from sqlalchemy.orm import Session

from backend.core.config import Settings
from backend.schemas.schemas import ProductModel
from backend.db.session import get_db
from backend.crud.querysets import get_product_by_id


def start_application(config: Settings):
    application = FastAPI(
        title=config.PROJECT_NAME,
        debug=True,
        version=config.PROJECT_VERSION,
        docs_url=f"{config.API_VERSION}/docs",
        redoc_url=f"{config.API_VERSION}/redoc"
    )
    return application


settings = Settings()

app = start_application(settings)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


@app.get('/')
def route():
    message = {"message": "test"}
    return Response(content=json.dumps(message), status_code=200)


@app.get('/{product_id}', response_model=ProductModel)
def get_product(product_id: int, db: Session = Depends(get_db)):
    if product := get_product_by_id(db, product_id):
        return product
    else:
        raise HTTPException(
            status_code=404,
            detail=f"product with {product_id} not found"
        )


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=settings.PROJECT_HOST,
        port=int(settings.PORT),
        reload=True
    )
