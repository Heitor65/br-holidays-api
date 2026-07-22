from app.models.Feriados import Feriados
from app.models.DayMonth import DayMonth

feriados_ac = [
    Feriados(id=101, name="Dia do Católico", date=DayMonth(day=20, month=1), description=" A data é um momento de reflexão, renovação da fé e celebração da comunidade católica acreana.").model_dump(),
    Feriados(id=102, name="Dia do Evangélico", date=DayMonth(day=23, month=1), description="Homenageia a comunidade evangélica local.").model_dump(),
    Feriados(id=103, name="Dia Internacional da Mulher", date=DayMonth(day=8, month=3), description="O reconhecimento do sufrágio universal, o acesso à educação e leis de proteção.").model_dump(),
    Feriados(id=104, name="Aniversário do Estado do Acre", date=DayMonth(day=15, month=6), description="Celebra a assinatura da lei que elevou o Acre à categoria de Estado, em 1962.").model_dump(),
    Feriados(id=105, name="Dia da Amazônia", date=DayMonth(day=5, month=9), description="Homenagem à criação da Província do Amazonas por Dom Pedro II, em 1850").model_dump(),
    Feriados(id=106, name="Tratado de Petrópolis", date=DayMonth(day=17, month=11), description="Celebra o tratado assinado em 1903 que incorporou oficialmente o território do Acre ao Brasil.").model_dump()
]

"""O Acre possui uma regra bem peculiar estabelecida pela Lei Estadual nº 2.126/2009: com exceção do aniversário do estado (15 de junho), qualquer outro feriado estadual que caia entre uma terça-feira e uma quinta-feira é adiado automaticamente para a sexta-feira daquela mesma semana, para evitar que o comércio e os serviços fiquem parando no meio dos dias úteis."""