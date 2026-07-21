from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_sp = [
    Feriados(name="Revolução Constitucionalista de 1932", date=DayMonth(day=9, month=7), description="Celebra a Data Magna do estado, que homenageia o início do levante armado de 1932 contra o governo de Getúlio Vargas.").model_dump()
]