from app.models.model_loader import load_model
import numpy as np

def predict(features: list[float]) -> float:
    model = load_model()

    input_array = np.array(features).reshape(1,-1)
    prediction = model.predict(input_array)

    return float(prediction[0])
