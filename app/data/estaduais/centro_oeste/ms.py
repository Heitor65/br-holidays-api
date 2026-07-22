from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth


feriados_ms = [
    Feriados(id=191, name="Criação do Estado de Mato Grosso do Sul", date=DayMonth(day=11, month=10), description="Comemora a criação do Estado de Mato Grosso do Sul, que ocorreu em 11 de outubro de 1977, quando foi desmembrado do estado de Mato Grosso.").model_dump(),
]