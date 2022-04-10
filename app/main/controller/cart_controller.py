from app.main.service.cart_service import checkout_cart, save_new_cart
from app.main.service.order_service import change_order_status
from app.main.util.decorator import token_required
from flask import request
from flask_restx import Resource

from ..util.dto import CartDto

api = CartDto.api
_cart = CartDto.cart

@api.route('/add')
class AddCart(Resource):
    @api.expect(_cart, validate=True)
    @api.response(200,'Cart created')
    @api.doc("create new cart")
    @token_required
    def post(self):
        # get the post data
        post_data = request.json
        return save_new_cart(data=post_data)

@api.route('/checkout')
class Checkout(Resource):
    @api.response(200,'Cart checked out')
    @api.doc("cart check out")
    @token_required
    def post(self):
        return checkout_cart()

@api.route('/updateStatus/<order_id>/<status>')
class Order(Resource):
    @api.response(201, 'Order update successfully.')
    @api.doc('Order update')
    def post(self,order_id,status):
        """Update status"""
        return change_order_status(order_id,status)
