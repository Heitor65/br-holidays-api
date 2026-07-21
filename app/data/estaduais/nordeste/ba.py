from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_ba = [
	Feriados(
		name="Independência da Bahia",
		date=DayMonth(day=2, month=7),
		description="Instituído pela Constituição Estadual, celebra a data mais importante do calendário baiano. O feriado relembra o dia em que as tropas brasileiras expulsaram definitivamente o exército português de Salvador, em 1823, consolidando a real independência do Brasil na região."
	).model_dump()
]