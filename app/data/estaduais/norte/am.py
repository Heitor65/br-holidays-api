from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_am = [
    Feriados(
        id=121,
        name="Elevação do Amazonas à Categoria de Província",
        date=DayMonth(day=5, month=9),
        description="Instituído como Data Magna do estado pela Lei Promulgada nº 231/2015, celebra o dia em que o Amazonas " \
        "se emancipou da Província do Grão-Pará, em 1850, tornando-se uma província independente.").model_dump()
    # 8 de dezembro (Dia de Nossa Senhora da Conceição), é feriado estadual apenas na área pública
]