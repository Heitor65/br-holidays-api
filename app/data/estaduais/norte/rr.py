from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_rr = [
	Feriado(
		name="Aniversário do Estado de Roraima",
		date=DayMonth(day=5, month=10),
		description="Celebra a Data Magna do estado, marcando o dia em que o território federal de Roraima foi elevado à categoria de Estado da Federação pela Constituição de 1988 (a instalação oficial do governo ocorreu em 1991)."
	).model_dump()
]