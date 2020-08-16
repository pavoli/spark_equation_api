from flask import Blueprint, jsonify, request

from app.models.products import Product

products_blueprint = Blueprint('products', __name__)


@products_blueprint.route('/products/', methods=['GET'])
def get_products():
    product_id = request.args.get('id')

    if product_id is None:
        result = get_all_products()
    else:
        result = get_product_by_id(product_id)

    return jsonify({
        'results': result
    })


@products_blueprint.route('/products/', methods=['DELETE'])
def delete_product():
    product_id = request.args.get('id')

    result = Product.query.filter_by(id=product_id).delete()

    return jsonify({
        'results': result
    })


def get_all_products():
    return [p.serialized for p in Product.query.all()]


def get_product_by_id(product_id):
    return [p.serialized for p in Product.query.filter_by(id=product_id)]