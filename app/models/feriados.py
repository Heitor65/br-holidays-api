from pydantic import BaseModel
from typing import Optional
from datetime import date

class feriado(BaseModel):
    name: str
    data: date
    description: str