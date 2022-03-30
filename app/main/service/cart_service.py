
from app.main import db
from app.main.model.cart import Cart
from typing import Dict


def save_new_cart(data: Dict[str, int]):
    # cart = Cart.query.filter_by(product_id=data['product_id']).first()
    # if cart:
        
    # else:
    #     response_object = {
    #         'status': 'fail',
    #         'message': 'Cart already exists.',
    #     }
    #     return response_object, 409

    new_cart = Cart(
            product_id=data['product-id'],
            quantity=data['quantity'],
        )
        
    return save_changes(new_cart)

def save_changes(data: Cart):
    db.session.add(data)
    db.session.commit()

