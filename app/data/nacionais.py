from app.models.Feriados import Feriado
from app.models.DayMonth import DayMonth

feriados_nacionais = [
    Feriado(name='Confraternização Universal (Ano Novo)', date=DayMonth(day = 1, month =1), description="Marca o início do ano novo. É um dia simbólico de renovação, celebração e união entre as pessoas.").model_dump(),
    Feriado(name='Tiradentes', date=DayMonth(day=21, month=4), description='Homenageia Joaquim José da Silva Xavier (Tiradentes), líder da Inconfidência Mineira e símbolo da luta pela independência do Brasil.').model_dump(),
    Feriado(name='Dia do Trabalho', date=DayMonth(day=1, month=5), description='Celebra as conquistas dos trabalhadores e os direitos trabalhistas.').model_dump(),
    Feriado(name='Independência do Brasil', date=DayMonth(day=7, month=9), description='Data em que o Brasil declarou sua independência de Portugal em 1822.').model_dump(),
    Feriado(name='Nossa Senhora Aparecida', date= DayMonth(day=12, month=10), description='Dia da padroeira do Brasil, muito importante para a fé católica no país.').model_dump(),
    Feriado(name='Finados', date=DayMonth(day=2, month=11), description='Dia dedicado à lembrança e homenagem aos falecidos.').model_dump(),
    Feriado(name='Proclamação da República', date=DayMonth(day=15, month=11), description='Marca a transição do Brasil de monarquia para república, em 1889.').model_dump(),
    Feriado(name='Dia da Consciência Negra', date=DayMonth(day=20, month=11), description='Homenageia Zumbi dos Palmares e reforça a luta contra o racismo e pela valorização da cultura negra.').model_dump(),
    Feriado(name='Natal', date=DayMonth(day=25, month=12), description='Celebra o nascimento de Jesus Cristo e é uma das datas mais importantes do cristianismo.').model_dump(),
    #Sexta-feira Santa
]

