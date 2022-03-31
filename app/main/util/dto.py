from importlib.metadata import requires
from flask_restx import Namespace, fields


class UserDto:
    api = Namespace('user', description='user related operations')
    user = api.model('user', {
        'username': fields.String(required=True, description='user username'),
        'password': fields.String(required=True, description='user password'),
        'user_id': fields.String(description='user Identifier')
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
        'productId': fields.String(required=True, description='id of product'),
        'quantity': fields.Integer(required=True, description='quantity of product'),
    })

