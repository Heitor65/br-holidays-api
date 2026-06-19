from pydantic import BaseModel
from typing import Optional
from DayMouth import day_month

class feriado(BaseModel):
    name : str
    date : day_month
    description : str