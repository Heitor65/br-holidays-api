from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_ap = [
    Feriados(name="Dia de São José", date=DayMonth(day=19, month=3), description="Celebra o Santo Padroeiro do Estado do Amapá.").model_dump(),
    Feriados(name="Dia de Cabralzinho", date=DayMonth(day=15, month=5), description="Celebra o Santo Padroeiro do Estado do Amapá.").model_dump(),
    Feriados(name="Criação do Território Federal do Amapá", date=DayMonth(day=13, month=9), description="Data Magna do estado, celebra o dia em que a região se desmembrou do Pará, em 1943, para se tornar um território federal independente.").model_dump()
]