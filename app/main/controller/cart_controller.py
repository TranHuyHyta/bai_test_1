from flask import request
from app.main.util.decorator import token_required
from flask_restx import Resource

# from app.main.util.decorator import admin_token_required
from ..util.dto import CartDto
from app.main.service.cart_service import save_new_cart, get_all_cart


api = CartDto.api
cart = CartDto.cart
# # get user infor

# data, status = Auth.get_logged_in_user(request)

# token = data.get('data')

# # get user - cart info

# user=User.query.filter_by(user_id=data.get("user_id")).first()

# cart_id=user.cart_id
# cart_items=Cart_Item.query.filter_by(cart_id=cart_id).all()

# find_product=False

# item_detail=None

# for item in cart_items:

# if(item.product_id==data.get("product_id")):

# find_product=True

# item_detail=item

# break

# if(find_product):

# item.quantity+=data.get("quantity")

# else:

# cart_item_new=Cart_Item(quantity=data.get("quantity",product_id=data.get("product_id")))

# save_changes(cart_item_new)
@api.route('/add')
# @api.param('user_id', 'The User identifier')
class AddCart(Resource):
    @api.doc("product related")
    # @token_required
    @api.expect(cart, validate=True)
    def post(self):
        # get the post data
        post_data = request.json
        return save_new_cart(data=post_data)

@api.route('/checkout')
class Checkout(Resource):
    @api.doc("cart related")
    @api.expect(cart, validate=True)
    def post(self):
        return get_all_cart()