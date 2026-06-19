from flask import jsonify, request, Blueprint
from pydantic import ValidationError
from app.db_mock.choices_feriados import feriados_nacionais

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/nacional', methods=['GET'])
def get_feriados_nacionais():
    return jsonify(feriados_nacionais), 200