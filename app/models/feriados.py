from pydantic import BaseModel
from typing import Optional
import DayMouth

class feriado(BaseModel):
    name : str
    date : DayMouth
    description : str