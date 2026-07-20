from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_ce = [
	Feriado(
		name="Data Magna do Ceará",
		date=DayMonth(day=25, month=3),
		description="Instituído pela Emenda Constitucional nº 69/2011, celebra o dia em que o Ceará se tornou a primeira província brasileira a abolir a escravidão, em 1884 — quatro anos antes da Lei Áurea, o que rendeu ao estado o famoso título de Terra da Luz, dado por José do Patrocínio."
	).model_dump()
]