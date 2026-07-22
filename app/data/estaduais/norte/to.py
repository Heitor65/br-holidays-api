from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_to = [
	Feriados(
		id=321,
		name="Padroeira do Estado (Nossa Senhora da Natividade)",
		date=DayMonth(day=8, month=9),
		description="Regulamentado pela Lei Estadual nº 627/1993, homenageia a padroeira oficial de Tocantins."
	).model_dump(),
	Feriados(
		id=322,
		name="Criação do Estado de Tocantins",
		date=DayMonth(day=5, month=10),
		description="Data Magna estadual instituída pela Lei Estadual nº 960/1998, comemora a promulgação da Constituição de 1988, que determinou a divisão de Goiás e a criação oficial do Tocantins."
	).model_dump(),
	Feriados(
		id=323,
		name="Dia do Senhor do Bonfim",
		date=DayMonth(day=15, month=8),
		description="Homenageia a tradicional Romaria do Senhor do Bonfim, uma festividade religiosa fortíssima na região que atrai milhares de romeiros e peregrinos desde o século XVIII."
	).model_dump(),
	Feriados(
		id=324,
		name="Autonomia do Estado",
		date=DayMonth(day=18, month=3),
		description="Instituído pela Lei Estadual nº 960/1998, celebra o dia em que o visconde de São João da Palma criou a comarca de São João das Duas Barras em 1809, marco inicial do desejo de separação da região do norte de Goiás."
	).model_dump()
]