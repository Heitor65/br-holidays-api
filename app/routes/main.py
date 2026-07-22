from flask import jsonify, request, Blueprint
from app.data.nacionais import feriados_nacionais
from app.data.estaduais import FERIADOS_POR_ESTADO
from app.utils.moveis import get_sexta_santa
from datetime import datetime

main_bp = Blueprint('main_bp', __name__)


def get_feriados_nacionais_com_moveis(ano):
  return feriados_nacionais + get_sexta_santa(ano)


def get_feriados_estaduais_por_uf(uf, ano):
  dado = FERIADOS_POR_ESTADO.get(uf.upper())
  if not dado:
    return None

  return dado(ano) if callable(dado) else dado

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
    dado = get_feriados_estaduais_por_uf(uf, request.args.get('ano', type=int, default=datetime.now().year))
    if not dado:
        return jsonify({"error": "UF não encontrada"}), 404
    return jsonify(dado), 200


@main_bp.route('/estaduais/<uf>/<int:feriado_id>', methods=['GET'])
def get_feriado_estadual_por_id(uf, feriado_id):
    """
    Retorna um feriado estadual específico pelo id.
    ---
    parameters:
      - name: uf
        in: path
        type: string
        required: true
        description: Sigla do estado em maiúsculo
        example: RJ
      - name: feriado_id
        in: path
        type: integer
        required: true
        description: Id do feriado
        example: 161
      - name: ano
        in: query
        type: integer
        required: false
        description: Ano para calcular feriados móveis estaduais
        example: 2025
    responses:
      200:
        description: Feriado encontrado
      404:
        description: Feriado ou UF não encontrada
    """
    ano = request.args.get('ano', type=int, default=datetime.now().year)
    dados = get_feriados_estaduais_por_uf(uf, ano)
    if not dados:
        return jsonify({"error": "UF não encontrada"}), 404

    feriado = next((item for item in dados if item.get('id') == feriado_id), None)
    if not feriado:
        return jsonify({"error": "Feriado não encontrado"}), 404

    return jsonify(feriado), 200

@main_bp.route('/nacional', methods=['GET'])
@main_bp.route('/nacionais', methods=['GET'])
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
    return jsonify(get_feriados_nacionais_com_moveis(ano)), 200


@main_bp.route('/nacional/<int:feriado_id>', methods=['GET'])
@main_bp.route('/nacionais/<int:feriado_id>', methods=['GET'])
def get_feriado_nacional_por_id(feriado_id):
    """
    Retorna um feriado nacional específico pelo id.
    ---
    parameters:
      - name: feriado_id
        in: path
        type: integer
        required: true
        description: Id do feriado
        example: 9
      - name: ano
        in: query
        type: integer
        required: false
        description: Ano para calcular a Sexta-feira Santa
        example: 2025
    responses:
      200:
        description: Feriado encontrado
      404:
        description: Feriado não encontrado
    """
    ano = request.args.get('ano', type=int, default=datetime.now().year)
    feriado = next((item for item in get_feriados_nacionais_com_moveis(ano) if item.get('id') == feriado_id), None)
    if not feriado:
        return jsonify({"error": "Feriado não encontrado"}), 404

    return jsonify(feriado), 200

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