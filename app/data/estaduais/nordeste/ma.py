from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_ma = [
	Feriado(
		name="Adesão do Maranhão à Independência do Brasil",
		date=DayMonth(day=28, month=7),
		description="Considerado a Data Magna do estado, esse feriado celebra o dia em que o Maranhão reconheceu oficialmente a independência do país, em 1823. Assim como aconteceu no Pará e na Bahia, a província maranhense não aderiu ao 7 de setembro imediatamente e precisou de intervenção militar para romper com Portugal."
	).model_dump(),
	Feriado(
		name="Dia Internacional da Mulher",
		date=DayMonth(day=8, month=3),
		description="Instituído por lei sancionada em março de 2026, no Maranhão."
	).model_dump()
]