
import uuid

from app.main.model.type_enum import TypeEnum

from .. import db


class Order(db.Model):
    __tablename__="order"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    order_id = db.Column(db.String(100), unique=True, default=lambda:uuid.uuid4())
    user_id = db.Column(db.String(100), unique=True)
    cart_items = db.relationship('Cart_Item', backref='cart', lazy='dynamic')

    type=db.Column(db.String(50), default=lambda:TypeEnum.Cart.value)
    payment_status=db.Column(db.String(100), nullable=True)
