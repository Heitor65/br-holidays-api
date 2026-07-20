from app.data.estaduais.centro_oeste.df import feriados_df
from app.data.estaduais.centro_oeste.ms import feriados_ms
from app.data.estaduais.nordeste.al import feriados_al
from app.data.estaduais.nordeste.ba import feriados_ba
from app.data.estaduais.nordeste.ce import feriados_ce
from app.data.estaduais.nordeste.ma import feriados_ma
from app.data.estaduais.nordeste.pb import feriados_pb
from app.data.estaduais.nordeste.pe import feriados_pe
from app.data.estaduais.nordeste.pi import feriados_pi
from app.data.estaduais.nordeste.rn import feriados_rn
from app.data.estaduais.nordeste.se import feriados_se
from app.data.estaduais.norte.ac import feriados_ac
from app.data.estaduais.norte.am import feriados_am
from app.data.estaduais.norte.ap import feriados_ap
from app.data.estaduais.norte.pa import feriados_pa
from app.data.estaduais.norte.ro import feriados_ro
from app.data.estaduais.norte.rr import feriados_rr
from app.data.estaduais.norte.to import feriados_to
from app.data.estaduais.sudeste.es import get_feriados_es
from app.data.estaduais.sudeste.rj import get_feriados_rj
from app.data.estaduais.sudeste.sp import feriados_sp
from app.data.estaduais.sul.rs import feriados_rs
from app.data.estaduais.sul.sc import feriados_sc


FERIADOS_POR_ESTADO = {
    "AC": feriados_ac,
    "AL": feriados_al,
    "AM": feriados_am,
    "AP": feriados_ap,
    "BA": feriados_ba,
    "CE": feriados_ce,
    "DF": feriados_df,
    "ES": get_feriados_es,
    "MA": feriados_ma,
    "MS": feriados_ms,
    "PA": feriados_pa,
    "PB": feriados_pb,
    "PE": feriados_pe,
    "PI": feriados_pi,
    "RJ": get_feriados_rj,
    "RN": feriados_rn,
    "RO": feriados_ro,
    "RR": feriados_rr,
    "RS": feriados_rs,
    "SC": feriados_sc,
    "SE": feriados_se,
    "SP": feriados_sp,
    "TO": feriados_to,
}