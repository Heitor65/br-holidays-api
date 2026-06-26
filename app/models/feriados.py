from pydantic import BaseModel
from typing import Optional
from app.models.DayMonth import day_month

class Feriado(BaseModel):
    name : str
    date : day_month
    description : str