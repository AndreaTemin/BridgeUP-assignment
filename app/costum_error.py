from fastapi import HTTPException

class WeightOutOfRangeException(HTTPException):
    def __init__(self, detail: str = "Weight of any entity must be between 0 and 100 extreems included"):
        super().__init__(status_code=400, detail=detail)

class NegativeWeightException(HTTPException):
    def __init__(self, detail: str = "Total weight cannot be negative"):
        super().__init__(status_code=400, detail=detail)

class NotFoundException(HTTPException):
    def __init__(self, detail: str = "Item not found"):
        super().__init__(status_code=404, detail=detail)

class InvalidCampaignTotalException(HTTPException):
    def __init__(self, detail: str = "Total campaign weight must equal 100 within the category"):
        super().__init__(status_code=400, detail=detail)