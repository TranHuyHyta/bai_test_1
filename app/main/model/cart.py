
from .. import db
import uuid

class Cart(db.Model):
    __tablename__="cart"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship("User", back_populates="cart")
    
    def __repr__(self):
        return "Cart: {}".format(self.name)

