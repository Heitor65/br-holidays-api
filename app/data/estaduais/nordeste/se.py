from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_se = [
	Feriados(
		name="Emancipação Política de Sergipe",
		date=DayMonth(day=8, month=7),
		description="Instituído pelo Artigo 269 da Constituição Estadual, celebra o dia em que Sergipe se tornou independente da Capitania da Bahia, em 1820, por meio de um decreto real de Dom João VI."
	).model_dump()
]