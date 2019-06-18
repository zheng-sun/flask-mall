from flask import Blueprint

bq = Blueprint('index', __name__, url_prefix='/index')

@bq.route('/list')
def list():
    return 'index list123131231233213'

@bq.route('/product_list')
def product_list():
    return 'product_list'

@bq.route('/productOne')
def productOne():
    return 'productOne'
