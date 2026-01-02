import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from app.api.schemas import PredictionRequest
from app.services.services import predict
from app.core.logging_config import setup_logging
import logging

load_dotenv()
setup_logging()
logger = logging.getLogger(__name__)

app = FastAPI(title = os.getenv("APP_NAME"))

@app.get("/health")
def health_check():
    return {"status":"ok",
            "environment":os.getenv("ENV")}

@app.post("/predict")
def predict(request: PredictionRequest):
    try:
        prediction = predict(request.features)
        logger.info(f"Prediction successful | features = len(request.features) | output = {prediction}")

        return {"status":"success", "prediction":prediction, "model_version":"v1"}
    
    except FileNotFoundError:
        raise HTTPException(status_code = 500, details = "File Not found")
    
    except Exception as e:
        logger.error("Prediction failed", exec_info = True)
        raise HTTPException(status_code=500, detail="Prediction Failed")
    




