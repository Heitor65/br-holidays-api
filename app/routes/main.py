from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from app.data.nacionais import feriados_nacionais
from app.data.estaduais import FERIADOS_POR_ESTADO
from app.utils.moveis import get_sexta_santa
from datetime import datetime

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/estaduais/<uf>', methods=['GET'])
def get_feriados_estadual(uf):
    dado = FERIADOS_POR_ESTADO.get(uf.upper())
    if not dado:
        return jsonify({"error": "UF não encontrada"}), 404
    
    ano = request.args.get('ano', type=int, default=datetime.now().year)
    
    if callable(dado):
        return jsonify(dado(ano)), 200
    return jsonify(dado), 200

@main_bp.route('/nacional', methods=['GET'])
def get_feriados_nacionais():
    ano = request.args.get('ano', type=int, default=datetime.now().year)
    return jsonify(feriados_nacionais + get_sexta_santa(ano)), 200