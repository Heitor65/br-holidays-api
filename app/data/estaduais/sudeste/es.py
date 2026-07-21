from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth
from app.utils.moveis import get_feriados_moveis


def get_feriados_es(ano: int) -> list[dict]:
    moveis_es = [f for f in get_feriados_moveis(ano)
                 if f["name"] == "Dia de Nossa Senhora da Penha"]
    return moveis_es