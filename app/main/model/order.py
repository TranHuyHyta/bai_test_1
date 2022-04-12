from marshmallow import Schema, fields
from .. import db

from app.main.model.cart_item import Cart_Item_Schema

class Order(db.Model):
    __tablename__="order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    order_id = db.Column(db.String(100), unique=True)
    user_id = db.Column(db.String(100))

    cart_items = db.relationship('Cart_Item', backref='order', lazy='dynamic')
    subtotal_ex_tax=db.Column(db.Float, nullable=True, default= 0)
    tax_total=db.Column(db.Float, nullable=True, default= 0)
    total=db.Column(db.Float, nullable=True, default= 0)

    payment_status=db.Column(db.String(100), nullable=True, default=None)

class Order_Schema(Schema):
    id = fields.Integer()
    cart_id = fields.String()
    user_id = fields.String()
    cart_items=fields.Nested(Cart_Item_Schema)