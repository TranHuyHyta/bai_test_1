
from marshmallow import Schema, fields
import uuid

from app.main.model.type_enum import TypeEnum
from app.main.model.cart_item import Cart_Item_Schema

from .. import db



class Cart(db.Model):
    __tablename__="cart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    cart_id = db.Column(db.String(100), unique=True, default=lambda:uuid.uuid4())
    order_id = db.Column(db.String(100), unique=True, default=None)
    user_id = db.Column(db.String(100), unique=True)
    cart_items = db.relationship('Cart_Item', backref='cart', lazy='dynamic')

    type=db.Column(db.String(50), default=lambda:TypeEnum.Cart.value)
    payment_status=db.Column(db.String(100), nullable=True)

class Cart_Schema(Schema):
    id = fields.Integer()
    cart_id = fields.String()
    user_id = fields.String()
    cart_items=fields.Nested(Cart_Item_Schema)
