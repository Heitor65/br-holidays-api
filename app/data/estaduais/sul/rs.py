from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth


feriados_rs = [
    Feriado(name="Dia do Gaúcho", date=DayMonth(day=20, month=9), description="Celebra a Data Magna gaúcha. A data homenageia o início da Revolução Farroupilha em 1835, o mais longo conflito civil da história do Brasil.").model_dump()
]