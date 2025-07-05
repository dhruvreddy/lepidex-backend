from fastapi import APIRouter, Depends

from dependency_injection import prediction_di

router = APIRouter(
    tags=["Predict"]
)

@router.post("/scan")
async def predict_api(result: dict = Depends(prediction_di)):
    return result