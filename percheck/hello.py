from flask import (Blueprint)

bp = Blueprint('hello', __name__,url_prefix='/')

@bp.route('/hello')
def hello():
    return 'Hello, World!'


