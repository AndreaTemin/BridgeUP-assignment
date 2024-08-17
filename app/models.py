from typing_extensions import Annotated
from pydantic import BaseModel, Field
from typing import Dict, Optional

Weight = Annotated[int, Field(ge=0, le=100)]

class Campaign(BaseModel):
    w: Weight

class Category(BaseModel):
    w: Weight
    campaigns: Optional[Dict[str, Campaign]] = None

class Source(BaseModel):
    w: Weight
    categories: Optional[Dict[str, Category]] = None

class WeightUpdate(BaseModel):
    w: Weight