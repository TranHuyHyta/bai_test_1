
from .. import db


class Product(db.Model):
    __tablename__="product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

    def __repr__(self):
        return "Product: {}".format(self.name)