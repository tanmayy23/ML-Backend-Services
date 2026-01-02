import joblib
import os
import logging

logger = logging.get(__name__)
MODEL_PATH = "model.pkl"
_model = None

def load_model():
    global _model

    if _model is None:
        logger.info("Loading model into the memory")
        if not os.path.exists(MODEL_PATH):
            logger.error("Model file not found")
            raise FileNotFoundError("Model file not found")
        
        _model = joblib.load(MODEL_PATH)
        logger.info("Model loaded successfully")
        
    return _model

