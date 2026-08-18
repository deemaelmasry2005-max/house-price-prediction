from fastapi import APIRouter, HTTPException
from app.schemas.prediction import PredictionRequest, PredictionResponse
from app.services.inference import model_service

router = APIRouter()

@router.get("/health")
def health_check():
    return {"status": "ok"}

@router.post("/predict", response_model=PredictionResponse)
def predict_price(payload: PredictionRequest):
    try:
        data = payload.model_dump()
        raw_price = model_service.predict(data)
        
        # تنسيق السعر بـ Lac / Cr
        if raw_price >= 10_000_000:
            formatted = f"₹ {raw_price / 10_000_000:.2f} Cr"
        elif raw_price >= 100_000:
            formatted = f"₹ {raw_price / 100_000:.2f} Lac"
        else:
            formatted = f"₹ {raw_price:,.2f}"

        return PredictionResponse(
            predicted_price=round(raw_price, 2),
            formatted_price=formatted
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))