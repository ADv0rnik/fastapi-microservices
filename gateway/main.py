import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from routes.routes import product_router
from config import Settings


settings = Settings()


def start_application(config: Settings):
    application = FastAPI(
        title=config.GATEWAY_NAME,
        debug=True
    )
    return application


app = start_application(settings)
app.include_router(product_router)
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGIN,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=settings.PROJECT_HOST,
        port=int(settings.GATEWAY_PORT),
        reload=True
    )
