from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_al = [
	Feriado(
		name="São João",
		date=DayMonth(day=24, month=6),
		description="Feriado estadual muito tradicional no Nordeste, celebrando o santo junino."
	).model_dump(),
	Feriado(
		name="São Pedro",
		date=DayMonth(day=29, month=6),
		description="Outra celebração do ciclo junino que é feriado oficial em todo o território alagoano."
	).model_dump(),
	Feriado(
		name="Emancipação Política de Alagoas",
		date=DayMonth(day=16, month=9),
		description="Data Magna do estado, que celebra o dia em que Alagoas se desmembrou da Capitania de Pernambuco, em 1817."
	).model_dump(),
	Feriado(
		name="Dia Estadual do Evangélico",
		date=DayMonth(day=30, month=11),
		description="Ao contrário do que acontece em estados como o Amapá (onde é apenas ponto facultativo), em Alagoas esta data é feriado civil oficial determinado por lei estadual, fechando o comércio e as empresas privadas."
	).model_dump()
]