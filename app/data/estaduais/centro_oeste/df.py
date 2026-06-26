from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth


feriados_df = [
    Feriado(name="Dia do Evangélico", date=DayMonth(day=30, month=11), description="Comemora a importância da comunidade evangélica no Distrito Federal e sua contribuição para a sociedade.").model_dump(),
]