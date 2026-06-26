from datetime import date, timedelta
from app.utils.pascoa import calcular_pascoa

def get_sexta_santa(ano: int) -> list[dict]:
    dia, mes = calcular_pascoa(ano)
    pascoa = date(ano, mes, dia)
    sexta = pascoa - timedelta(days=2)
    return [{
        "name": "Sexta-feira Santa",
        "date": {"day": sexta.day, "month": sexta.month},
        "description": "Celebra a crucificação de Jesus Cristo."
    }]

def get_feriados_moveis(ano: int) -> list[dict]:
    dia, mes = calcular_pascoa(ano)
    pascoa = date(ano, mes, dia)
    moveis = [
        ("Terça-feira de Carnaval", pascoa - timedelta(days=47), "Último dia do Carnaval."),
        ("Corpus Christi", pascoa + timedelta(days=60), "Celebra a presença de Cristo na Eucaristia."),
        ("Dia de Nossa Senhora da Penha", pascoa + timedelta(days=8), "O Dia de Nossa Senhora da Penha é uma festividade religiosa católica dedicada à Virgem Maria")
    ]
    return [
        {"name": nome, "date": {"day": d.day, "month": d.month}, "description": desc}
        for nome, d, desc in moveis
    ]