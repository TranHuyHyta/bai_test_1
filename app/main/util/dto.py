from importlib.metadata import requires
from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password')
    })


class AuthDto:
    api = Namespace('auth', description='authentication related operations')
    user_auth = api.model('auth_details', {
        'username': fields.String(required=True, description='username'),
        'password': fields.String(required=True, description='The user password '),
    })

class CartDto:
    api = Namespace('cart', description='cart related operations')
    cart = api.model('cart', {
        'product_id': fields.String(required=True, description='product_id'),
        'quantity': fields.Integer(required=True, description='quantity'),
    })

class CartItemDto:
    api = Namespace('cart_item', description='cart item string data to update,delete')
    cart_item_id = api.model('cart_item_change_qty', {
        'quantity': fields.Integer(required=True, description='quantity')
    })
