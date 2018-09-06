from db import db

class SnacksModel(db.Model):
    __tablename__ = 'snacks'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    description = db.Column(db.Text, nullable=False)
    price = db.Column(db.Integer)
    img = db.Column(db.String, nullable=False, default='')
    is_perishable = db.Column(db.Boolean, nullable=False, default=False)

    reviews = db.relationship('ReviewsModel', lazy='dynamic')

    def __init__(self, name, description, price, img, is_perishable):
        self.name = name
        self.description = description
        self.price = price
        self.img = img
        self.is_perishable = is_perishable

    def json(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'price': self.price, 'img': self.img, 'is_perishable': self.is_perishable, 'reviews': [review.json() for review in self.reviews.all()]}

    def json2(self):
        return {'id': self.id, 'name': self.name, 'description': self.description, 'price': self.price, 'img': self.img, 'is_perishable': self.is_perishable}

    @classmethod
    def find_by_id(cls, id):
        return cls.query.filter_by(id=id).first()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
