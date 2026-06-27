from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_pi = [
	Feriado(
		name="Dia do Batalhão de Jenipapo",
		date=DayMonth(day=13, month=3),
		description="Instituído pela Lei Estadual nº 5.439/2005, homenageia os piauienses que lutaram e morreram na Batalha do Jenipapo em 1823, em Campo Maior. Foi uma das batalhas mais sangrentas da Independência do Brasil, onde lavradores e artesãos locais enfrentaram as tropas profissionais portuguesas."
	).model_dump(),
	Feriado(
		name="Dia do Piauí (Data Magna)",
		date=DayMonth(day=19, month=10),
		description="Celebra o dia em que a província do Piauí proclamou sua adesão à Independência do Brasil, em 1822, na cidade de Parnaíba, sob a liderança de Simplício Dias da Silva."
	).model_dump()
]