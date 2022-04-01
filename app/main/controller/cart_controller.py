from app.main.service.cart_service import checkout_cart, save_new_cart
from app.main.util.decorator import token_required
from flask import request
from flask_restx import Resource

from ..util.dto import CartDto

api = CartDto.api
_cart = CartDto.cart

@api.route('/add')
class AddCart(Resource):
    @api.expect(_cart, validate=True)
    @api.response(201,'Cart created')
    @api.doc("create new cart")
    @token_required
    def post(self):
        # get the post data
        post_data = request.json
        return save_new_cart(data=post_data)

@api.route('/checkout')
class Checkout(Resource):
    @api.response(201,'Cart checkouted')
    @api.doc("cart checkout")
    @token_required
    def post(self):
        return checkout_cart()
