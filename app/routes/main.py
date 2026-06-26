from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from app.data.nacionais import feriados_nacionais
from app.data.estaduais import FERIADOS_POR_ESTADO

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/nacional', methods=['GET'])
def get_feriados_nacionais():
    return jsonify(feriados_nacionais), 200

@main_bp.route('/estaduais/<uf>', methods=['GET'])
def get_feriados_estadual(uf):
    feriados = FERIADOS_POR_ESTADO.get(uf.upper())
    if not feriados:
        return jsonify({"error": "UF não encontrada"}), 404
    return jsonify(feriados), 200