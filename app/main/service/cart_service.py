
import uuid

from app.main import db
from app.main.model.cart import Cart, Cart_Schema
from app.main.model.cart_item import Cart_Item, Cart_Item_Schema
from app.main.model.order import Order, Order_Schema
from app.main.model.product import Product
from app.main.enum.type_enum import TypeEnum
from app.main.service.auth_helper import Auth
from flask import json, request

cart_schema=Cart_Schema()
cart_item_schema=Cart_Item_Schema()
order_schema=Order_Schema()

def respond_cart(user_id):
    cart = Cart.query.filter_by(user_id=user_id).first()

    obj = {
        "cart_id" : cart.cart_id,
        "user_id" : cart.user_id,
        "cart_item": None,
        "subtotal_ex_tax": 0,
        "tax_total": 0,
        "total": 0
    }
    obj["subtotal_ex_tax"]=sum(item.subtotal_ex_tax for item in cart.cart_items)
    obj["tax_total"]=sum(item.tax_total for item in cart.cart_items)
    obj["total"]=sum(item.total for item in cart.cart_items)

    obj["cart_item"]=[json.loads(cart_item_schema.dumps(item)) for item in cart.cart_items]

    return obj

def respond_order(user_id):
    order = Order.query.filter_by(user_id=user_id)
    order = Order.query.filter_by(user_id=user_id).all()
    if len(order)>1:
        last_order = order[-1]
    else:
        last_order = Order.query.filter_by(user_id=user_id).first()
    obj = {
        "order_id" : last_order.order_id,
        "user_id" : last_order.user_id,

        "cart_item": None,
        "subtotal_ex_tax": 0,
        "tax_total": 0,
        "total": 0
    }
    obj["subtotal_ex_tax"]=sum(item.subtotal_ex_tax for item in last_order.cart_items)
    obj["tax_total"]=sum(item.tax_total for item in last_order.cart_items)
    obj["total"]=sum(item.total for item in last_order.cart_items)

    obj["cart_item"]=[json.loads(cart_item_schema.dumps(item)) for item in last_order.cart_items]

    
    obj["payment_status"]=last_order.payment_status

    return obj

def cart_recalc(user_id):
    cart= Cart.query.filter_by(user_id=user_id).first()
    cart_items=Cart_Item.query.filter_by(cart_id=cart.id).all()
    cart.subtotal_ex_tax = sum(row.subtotal_ex_tax for row in cart_items)
    cart.tax_total = sum(row.tax_total for row in cart_items)
    cart.total = sum(row.total for row in cart_items)
    db.session.commit()

def save_new_cart(data):
    user_id=Auth.user_cart_by_id(request)
    if user_id:
        cart_data=Cart.query \
            .filter_by(type=TypeEnum.Cart.value) \
            .filter_by(user_id=user_id).first()
        product=Product.get_product_by_uuid(data.get("product_id"))
        if not product: 
            return {"message":"could not found product with input id!!!"}, 403

        if cart_data:
            cart_items=Cart_Item.query.filter_by(cart_id=cart_data.id,
            product_id=data.get("product_id")).all()
            if cart_items:
                for itm in cart_items:
                    tmp=Product.get_product_by_uuid(itm.product_id)
                    quantity=itm.quantity + int(data.get("quantity"))
                    itm.quantity = quantity

                    sub_total=quantity*tmp.price
                    itm.subtotal_ex_tax=sub_total

                    tax_total=(sub_total*10)/100

                    itm.tax_total=tax_total
                    itm.total=sub_total+tax_total
            else:
                cart_item=Cart_Item()
                cart_item.cart_id=cart_data.id

                cart_item.product_id = data.get("product_id")
                cart_item.subtotal_ex_tax=int(data.get("quantity"))

                sub_total=int(data.get("quantity"))*product.price
                cart_item.subtotal_ex_tax=sub_total

                tax_total=(sub_total*10)/100
                cart_item.tax_total=tax_total

                cart_item.total=sub_total+tax_total
                cart_item.quantity=int(data.get("quantity"))
                db.session.add(cart_item)

            db.session.commit()
            cart_recalc(user_id)
            # return data as required
            return respond_cart(user_id), 200
        else:
            cart_data=Cart()
            cart_data.cart_uuid=uuid.uuid4()
            cart_data.user_id=user_id

            cart_item=Cart_Item()
            cart_item.product_id=data.get("product_id")
            cart_item.order_product_uuid=data.get("product_id")

            sub_total=int(data.get("quantity"))*product.price
            cart_item.subtotal_ex_tax=sub_total

            cart_item.quantity=int(data.get("quantity"))
            tax_total=(sub_total*10)/100
            cart_item.tax_total=tax_total
            cart_item.total=sub_total+tax_total

            cart_data.cart_items.append(cart_item)
            save_changes(cart_data)
            cart_recalc(user_id)
            # return data as required
            return respond_cart(user_id), 200

    return {"message":"Bad request!!!"}, 403

def change_cart_quantity(cart_item_id,data):
    user_id=Auth.user_cart_by_id(request)
    if user_id:
        cart_data=Cart.query.filter_by(user_id=user_id).first()
        if cart_data:
            cart_item=Cart_Item.query.filter_by(cart_item_id=cart_item_id).first()
            if cart_item:
                product=Product.query.filter_by(product_id=cart_item.product_id).first()
                # calculate values for cart-item
                if not product:
                    return {"message":"Bad request!!!"}, 403
                
                cart_item.quantity += int(data.get("quantity"))

                cart_item.subtotal_ex_tax = int(cart_item.quantity)*product.price

                cart_item.tax_total =(int(cart_item.subtotal_ex_tax)*10)/100

                cart_item.total=int(cart_item.subtotal_ex_tax)+int(cart_item.tax_total)

                db.session.commit()
                # return data as required
                return respond_cart(user_id), 200

    return {"message":"Bad request!!!"}, 403


def checkout_cart():
    user_id=Auth.user_cart_by_id(request)
    if user_id:
        cart_data=Cart.query.filter_by(user_id=user_id).first()
        if cart_data:
            order_data= Order()

            order_data.payment_status="INIT"
            order_data.order_id = str(uuid.uuid4())
            order_data.user_id = cart_data.user_id

            order_data.subtotal_ex_tax = cart_data.subtotal_ex_tax
            order_data.tax_total = cart_data.tax_total
            order_data.total = cart_data.total 

            save_changes(order_data)
            
            for item in cart_data.cart_items:
                item.type = TypeEnum.OrderDetail.value
                item.order_id = order_data.id
            db.session.delete(cart_data)
            db.session.commit()
            # update cart price
            return respond_order(user_id), 200
        else:
            return {"message" : "No cart data"}, 400
    return {"message" : "PLease login"}, 403

def delete_cart_item(cart_item_id):
    user_id = Auth.user_cart_by_id(request)
    if user_id:
        cart = Cart.query.filter_by(user_id=user_id).first()
        if cart:
            cart_item_id_order = Cart_Item.query.filter_by(cart_item_id=cart_item_id)\
                .filter_by(type=TypeEnum.OrderDetail.value).first()
            
            cart_item_id_cart_item = Cart_Item.query.filter_by(cart_item_id=cart_item_id)\
                .filter_by(type=TypeEnum.Cart_Item.value).first()

            if cart_item_id_order:
                return {"message": "Order item can't be delete"}, 403
            if cart_item_id_cart_item:
                db.session.delete(cart_item_id_cart_item)

            db.session.commit()

            return respond_cart(user_id),200
    return {"message":"Bad request!!!"}, 403


def save_changes(data: Cart):
    db.session.add(data)
    db.session.commit()

