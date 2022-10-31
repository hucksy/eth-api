from app.eth_api import models
from app.database import engine
from app.eth_api import create_app
import uvicorn

app = create_app()
models.Base.metadata.create_all(bind=engine)

if __name__ == "__main__":
    uvicorn.run("app.main:app", port=5000, reload=True)
