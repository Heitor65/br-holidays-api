from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth
from app.utils.moveis import get_feriados_moveis

feriados_rj = [
    Feriados(name="Dia de São Jorge", date = DayMonth(day=23, month=4), description="Homenageia o Santo Guerreiro, símbolo de resistência e fé, celebrado pelo sincretismo com Ogum").model_dump(),
]

def get_feriados_rj(ano: int = None) -> list[dict]:
    if ano:
        moveis_rj = [f for f in get_feriados_moveis(ano) 
                     if f["name"] in ["Terça-feira de Carnaval", "Corpus Christi"]]
        return feriados_rj + moveis_rj
    return feriados_rj