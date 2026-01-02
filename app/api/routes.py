from fastapi import APIRouter, HTTPException
from app.api.schemas import PredictionRequest
from app.services.inference import predict
from app.core.logging_config import setup_logging
import logging

router = APIRouter()
setup_logging()
logger = logging.getLogger(__name__)

@router.post("/predict")
def predict(requests: PredictionRequest):
    logger.info("Prediction request received")
    try:
        prediction = predict(requests.features)
        return {"status":"success", "prediction": prediction, "model_version": "v1"}
    
    except Exception:
        logger.error("Prediction failed", exc_info=True)
        raise HTTPException(status_code=500, detail="Prediction failed")
