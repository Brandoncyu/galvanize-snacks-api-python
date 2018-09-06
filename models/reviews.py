from db import db

class ReviewsModel(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    text = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)


    snack_id = db.Column(db.Integer, db.ForeignKey('snacks.id'))
    snack = db.relationship('SnacksModel')

    def __init__(self, title, text, rating, snack_id):
        self.title = title
        self.text = text
        self.rating = rating
        self.snack_id = snack_id

    def json(self):
        return {'id': self.id, 'title': self.title, 'text': self.text, 'rating': self.rating, 'snack_id': self.snack_id }

    @classmethod
    def find_by_rev_id(cls, id):
        return cls.query.filter_by(id=id).first() #SELECT * FROM items WHERE name=name #query comes from sqlalchemy

    def save_to_db(self):
        db.session.add(self) #collection of objects that we add to database
        db.session.commit()


    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
