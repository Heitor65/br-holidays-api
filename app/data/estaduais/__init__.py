from centro_oeste.df import feriados_df
from centro_oeste.ms import feriados_ms
from sudeste.sp import feriados_sp
from sudeste.rj import feriados_rj
from sul.rs import feriados_rs
from sul.sc import feriados_sc


FERIADOS_POR_ESTADO = {
    "DF": feriados_df,
    "MS": feriados_ms,
    "SP": feriados_sp,
    "RJ": feriados_rj,
    "RS": feriados_rs,
    "SC": feriados_sc
}