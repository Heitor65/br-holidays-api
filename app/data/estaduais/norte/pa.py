from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_pa = [
	Feriados(
		name="Dia da Adesão do Pará à Independência do Brasil",
		date=DayMonth(day=15, month=8),
		description="Instituído pela Lei Estadual nº 5.999/1996, celebra a Data Magna do estado. Essa data marca o dia em que o Pará finalmente aceitou a independência do Brasil (em 1823), quase um ano após o grito do Ipiranga, sendo a última província a se integrar ao novo Império."
	).model_dump()
]


# 8 de dezembro (Dia de Nossa Senhora da Conceição), é feriado estadual apenas na área pública
