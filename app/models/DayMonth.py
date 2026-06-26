from pydantic import BaseModel

class DayMonth(BaseModel):
    day : int
    month : int