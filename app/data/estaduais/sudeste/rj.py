from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_rj = [
    Feriado(name="Dia de São Jorge", date = DayMonth(day=23, month=4), description="Homenageia o Santo Guerreiro, símbolo de resistência e fé, celebrado pelo sincretismo com Ogum").model_dump(),
    #Terça-feira de Carnaval,
    #Corpus Christi
]