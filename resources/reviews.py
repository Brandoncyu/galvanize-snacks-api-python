import sqlite3
from flask_restful import Resource, reqparse
from models.reviews import ReviewsModel
from models.snacks import SnacksModel

class Reviews(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('text',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('rating',
        type=int
    )

    def post(self, snack_id):
        data = Reviews.parser.parse_args()
        review = ReviewsModel(data['title'], data['text'], data['rating'], snack_id)

        review.save_to_db()

        return {'data': review.json()}, 201

class ReviewsList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('title',
        type=str
    )
    parser.add_argument('text',
        type=str
    )
    parser.add_argument('rating',
        type=int
    )

    def patch(self, snack_id, rev_id):
        snacks = SnacksModel.find_by_id(snack_id)
        if snacks is None:
            return {'message': 'Snack with provided ID is not found'}, 404
        reviews = ReviewsModel.find_by_rev_id(rev_id)
        if reviews is None:
            return {'message': 'Review with provided ID is not found'}, 404

        data = ReviewsList.parser.parse_args()
        if data['title']:
            reviews.title = data['title']
        if data['text']:
            reviews.text = data['text']
        if data['rating']:
            reviews.rating = data['rating']

        reviews.save_to_db()

        return {'data': reviews.json()}, 200

    def delete(self, snack_id, rev_id):
        snacks = SnacksModel.find_by_id(snack_id)
        if snacks is None:
            return {'message': 'Snack with provided ID is not found'}, 404
        reviews = ReviewsModel.find_by_rev_id(rev_id)
        if reviews is None:
            return {'message': 'Review with provided ID is not found'}, 404

        reviews.delete_from_db()

        return {'message': 'Review Deleted'}, 202
