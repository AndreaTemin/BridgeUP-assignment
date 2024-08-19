from fastapi import HTTPException


class WeightOutOfRangeException(HTTPException):
    def __init__(self, detail: str = "Weight must be between 0 and 100"):
        super().__init__(status_code=400, detail=detail)
