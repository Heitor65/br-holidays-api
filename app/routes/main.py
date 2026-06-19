from flask import jsonify, request, blueprints
from pydantic import ValidationError

main_bp = blueprints('main_bp', __name__)

@main_bp.route('/nacional', methods=['GET'])
def get_feriados_nacionais():
    return 