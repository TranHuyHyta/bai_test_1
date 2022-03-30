import uuid

from sqlalchemy.dialects.postgresql import UUID

from .. import db


class Product(db.Model):
    __tablename__="Product"

    id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    name = db.Column(db.String(100))
    price = db.Column(db.Integer)

    def __repr__(self):
        return "Product: {}".format(self.name)