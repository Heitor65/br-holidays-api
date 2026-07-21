from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_ro = [
	Feriados(
		name="Criação e Instalação do Estado de Rondônia",
		date=DayMonth(day=4, month=1),
		description="Regulamentado pela Lei Estadual nº 2.291/2010, celebra a data em que o estado foi oficialmente instalado e sua transição de território federal para estado da federação (ocorrida originalmente em 1982)."
	).model_dump()
]