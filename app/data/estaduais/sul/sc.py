from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth


feriados_sc = [
    Feriado(name="Data Magna do Estado de Santa Catarina", date=DayMonth(day=11, month=8), description="Celebra a criação da capitania de Santa Catarina (sua emancipação política em 1738).").model_dump()  # Se cair em dia util o feriado é transferido para domingo
]