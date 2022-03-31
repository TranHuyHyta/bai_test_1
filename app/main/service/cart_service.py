
from itertools import product
from statistics import quantiles

from app.main import db
from app.main.model.cart import Cart
from app.main.model.user import User
from typing import Dict

user_id = User.id

def save_new_cart(data: Dict[str, int]):
    cart = Cart.query.filter_by(user_id=data['user_id']).first()
    if not cart:
        new_cart = Cart(
            productId=data['productId'],
            quantity=data['quantity'],
        )
        save_changes(new_cart)
    else:
        
        update = cart['quantity'] + data['quantity']
        return save_changes(update)

def get_all_cart():
    return Cart.query.all()


def save_changes(data: Cart):
    db.session.add(data)
    db.session.commit()

