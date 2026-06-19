from app.models.feriados import feriado
from app.models.DayMonth import day_month

feriados_nacionais = [
    feriado(name='Confraternização Universal (Ano Novo)', date=day_month(day = 1, month =1), description="Marca o início do ano novo. É um dia simbólico de renovação, celebração e união entre as pessoas.").model_dump(),
    feriado(name='Tiradentes', date=day_month(day=21, month=4), description='Homenageia Joaquim José da Silva Xavier (Tiradentes), líder da Inconfidência Mineira e símbolo da luta pela independência do Brasil.').model_dump(),
    feriado(name='Dia do Trabalho', date=day_month(day=1, month=5), description='Celebra as conquistas dos trabalhadores e os direitos trabalhistas.').model_dump(),
    feriado(name='Independência do Brasil', date=day_month(day=7, month=9), description='Data em que o Brasil declarou sua independência de Portugal em 1822.').model_dump(),
    feriado(name='Nossa Senhora Aparecida', date= day_month(day=12, month=10), description='Dia da padroeira do Brasil, muito importante para a fé católica no país.').model_dump(),
    feriado(name='Finados', date=day_month(day=2, month=11), description='Dia dedicado à lembrança e homenagem aos falecidos.').model_dump(),
    feriado(name='Proclamação da República', date=day_month(day=15, month=11), description='Marca a transição do Brasil de monarquia para república, em 1889.'),
    feriado(name='Dia da Consciência Negra', date=day_month(day=20, month=11), description='Homenageia Zumbi dos Palmares e reforça a luta contra o racismo e pela valorização da cultura negra.').model_dump(),
    feriado(name='Natal', date=day_month(day=25, month=12), description='Celebra o nascimento de Jesus Cristo e é uma das datas mais importantes do cristianismo.').model_dump()
]

