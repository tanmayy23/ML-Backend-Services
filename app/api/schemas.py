from pydantic import BaseModel, Field, field_validator
from typing import List

class PredictionRequest(BaseModel):
    features: List[float] = Field(..., min_items = 1, description = "List of numeric float values")
    @field_validator('features')
    @classmethod
    def check_feature(cls, v):
        if len(v) != 3:
            raise ValueError('Model must contain exactly 3 float values')
        return v
    