import time
import logging
import numpy as np
from app.models.model_loader import load_model

logger = logging.getLogger(__name__)

def predict(features: list[float]) -> float:
    start_time = time.time()

    model = load_model()
    input_array = np.array(features).reshape(1,-1)
    prediction = model.predict(input_array)

    latency = time.time() - start_time
    logger.info(f"Inferenece Latency: {latency:.4f} seconds")

    return float(prediction[0])
