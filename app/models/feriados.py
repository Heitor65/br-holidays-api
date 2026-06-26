from pydantic import BaseModel
from typing import Optional
from app.models.DayMonth import DayMonth

class Feriado(BaseModel):
    name : str
    date : DayMonth
    description : str