from fastapi import FastAPI, Depends
from app.config import get_env_configs


def create_app() -> FastAPI:
    app = FastAPI()

    from .router import eth_router
    app.include_router(eth_router)

    @app.get("/")
    async def root():
        return {"message": "hulloh beautiful world!"}

    return app
