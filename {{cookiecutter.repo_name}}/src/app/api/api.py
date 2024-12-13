from fastapi import APIRouter

api_router = APIRouter()

@api_router.get("/hello", status_code=200)
async def predict():
    return {"status": "OK"}
