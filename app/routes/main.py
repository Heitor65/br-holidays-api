from flask import jsonify, request, Blueprint
from pydantic import ValidationError

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/nacional', methods=['GET'])
def get_feriados_nacionais():
    return 