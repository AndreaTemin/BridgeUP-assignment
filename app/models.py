from typing_extensions import Annotated
from pydantic import BaseModel, Field, field_validator
from typing import Dict, Optional
from app.costum_error import WeightOutOfRangeException

# Weight = Annotated[int, Field(ge=0, le=100)]

class Campaign(BaseModel):
    w: int

class Category(BaseModel):
    w: int
    campaigns: Optional[Dict[str, Campaign]] = None

class Source(BaseModel):
    w: int
    categories: Optional[Dict[str, Category]] = None

class WeightUpdate(BaseModel):
    w: int

    @field_validator("w")
    def validate_weight(cls, value):
        if value < 0 or value > 100:
            raise WeightOutOfRangeException
        return value