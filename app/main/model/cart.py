
from .. import db

class Cart(db.Model):
    __tablename__="cart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(100), unique=True)
    quantity = db.Column(db.Integer)

    def __repr__(self):
        return "Cart: {}".format(self.name)

