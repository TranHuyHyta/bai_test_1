
from .. import db

import uuid

class Product(db.Model):
    __tablename__="product"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    product_id = db.Column(db.String(100), unique=True, default=lambda: uuid.uuid4())
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

    @staticmethod
    def get_product_by_uuid(product_id):
        return Product.query.filter_by(product_id=product_id).first()

    def __init__(self, data):
        self.name = data.get("name")
        self.price = data.get("price")
        self.product_id = data.get("product_id")

    def __repr__(self):
        return "Product: {}".format(self.name)