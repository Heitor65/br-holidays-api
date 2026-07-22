from pydantic import BaseModel
from app.models.DayMonth import DayMonth

class Feriados(BaseModel):
    id : int
    name : str
    date : DayMonth
    description : str