from app.main import db
from app.main.model.cart import Cart

def change_order_status(order_id, status):
    print(order_id)
    order_data = Cart.query.filter_by(order_id=order_id).first()
    print(order_data.payment_status)
    order_data.payment_status = status
    db.session.commit()
    return {
        "Order": order_data,
        "new_status": status
    } ,200