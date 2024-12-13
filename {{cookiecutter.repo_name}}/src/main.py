from fastapi import FastAPI

from app.api.api import api_router
from app.api.heartbeat import heartbeat_router
from app.core.config import settings

VERSION_PREFIX = settings.API_V1_STR

app = FastAPI(title=settings.PROJECT_NAME)

app.include_router(heartbeat_router)
app.include_router(api_router, prefix=VERSION_PREFIX, tags=["ML API"])

if __name__ == "__main__":
    # Use this for debugging purposes only
    import uvicorn

    uvicorn.run("main:app", reload=True, host="0.0.0.0", port=8001, log_level="debug")
