from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_rn = [
	Feriados(
		name="Dia dos Santos Mártires de Cunhaú e Uruaçu",
		date=DayMonth(day=3, month=10),
		description="Instituído pela Lei Estadual nº 8.913/2006, é o feriado dos padroeiros do estado. A data homenageia os cerca de 30 fiéis que foram cruelmente assassinados em 1645 por tropas holandesas e índios aliados por se recusarem a abandonar a fé católica. O grupo foi oficialmente canonizado pelo Papa Francisco em 2017 como os primeiros mártires do Brasil."
	).model_dump()
]