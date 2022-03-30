from flask import request
from flask_restx import Resource

# from app.main.util.decorator import admin_token_required
from ..util.dto import CartDto
from app.main.service.cart_service import save_new_cart


api = CartDto.api
cart = CartDto.cart

@api.route('/add')
class AddCart(Resource):
    @api.doc("product related")
    @api.expect(cart, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return save_new_cart(data=post_data)
