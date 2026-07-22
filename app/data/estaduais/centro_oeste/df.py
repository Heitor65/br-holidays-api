from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth


feriados_df = [
    Feriados(id=161, name="Dia do Evangélico", date=DayMonth(day=30, month=11), description="Comemora a importância da comunidade evangélica no Distrito Federal e sua contribuição para a sociedade.").model_dump(),
]