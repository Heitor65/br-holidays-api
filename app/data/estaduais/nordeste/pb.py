from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_pb = [
    Feriado(
        name="Fundação da Paraíba",
        date=DayMonth(day=5, month=8),
        description="Instituído pela Lei Estadual nº 10.601/2015, celebra a fundação da Paraíba, ocorrida em 5 de agosto de 1585, " \
        "quando o capitão-mor João Tavares foi nomeado para governar a capitania. A data é considerada a Data Magna do estado."
    ).model_dump()
]