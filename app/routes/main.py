from flask import jsonify, request, Blueprint
from app.data.nacionais import feriados_nacionais
from app.data.estaduais import FERIADOS_POR_ESTADO
from app.utils.moveis import get_sexta_santa
from datetime import datetime

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/estaduais/<uf>', methods=['GET'])
def get_feriados_estadual(uf):
    """
    Retorna os feriados estaduais de uma UF.
    ---
    parameters:
      - name: uf
        in: path
        type: string
        required: true
        description: Sigla do estado em maiúsculo
        example: RJ
      - name: ano
        in: query
        type: integer
        required: false
        description: Ano para calcular feriados móveis estaduais
        example: 2025
    responses:
      200:
        description: Lista de feriados do estado
      404:
        description: UF não encontrada
    """
    dado = FERIADOS_POR_ESTADO.get(uf.upper())
    if not dado:
        return jsonify({"error": "UF não encontrada"}), 404
    
    ano = request.args.get('ano', type=int, default=datetime.now().year)
    
    if callable(dado):
        return jsonify(dado(ano)), 200
    return jsonify(dado), 200

@main_bp.route('/nacional', methods=['GET'])
def get_feriados_nacionais():
    """
    Retorna os feriados nacionais.
    ---
    parameters:
      - name: ano
        in: query
        type: integer
        required: false
        description: Ano para calcular a Sexta-feira Santa
        example: 2025
    responses:
      200:
        description: Lista de feriados nacionais
    """
    ano = request.args.get('ano', type=int, default=datetime.now().year)
    return jsonify(feriados_nacionais + get_sexta_santa(ano)), 200

@main_bp.route('/health', methods=['GET'])
def health_check():
    """
    Endpoint de verificação de saúde da API.
    ---
    responses:
      200:
        description: API está funcionando corretamente
    """
    return jsonify({"status": "API está funcionando corretamente"}), 200