from app.data.estaduais.centro_oeste.df import feriados_df
from app.data.estaduais.centro_oeste.ms import feriados_ms
from app.data.estaduais.sudeste.sp import feriados_sp
from app.data.estaduais.sudeste.rj import feriados_rj
from app.data.estaduais.sul.rs import feriados_rs
from app.data.estaduais.sul.sc import feriados_sc


FERIADOS_POR_ESTADO = {
    "DF": feriados_df,
    "MS": feriados_ms,
    "SP": feriados_sp,
    "RJ": feriados_rj,
    "RS": feriados_rs,
    "SC": feriados_sc
}