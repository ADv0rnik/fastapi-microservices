import json
import uvicorn

from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import Response

from app.core.config import Settings


def start_application(config: Settings):
    application = FastAPI(
        title='payment',
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
async def route():
    message = {"message": "test"}
    return Response(content=json.dumps(message), status_code=200)


if __name__ == '__main__':
    uvicorn.run(
        app="main:app",
        host=settings.PROJECT_HOST,
        port=8080,
        reload=True
    )
