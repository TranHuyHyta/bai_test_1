from .. import db

class Cart_Item(db.Model):
    __tablename__="cart_item"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    cart_id = db.Column(db.Integer, db.ForeignKey('cart.id'))
    productId = db.Column(db.String(100), unique=True)
    quantity = db.Column(db.Integer)
    subtotal_ex_tax = db.Column(db.Float)
    tax_total = db.Column(db.Float)
    total=db.Column(db.Float)


    def __repr__(self):
        return "Cart: {}".format(self.name)

