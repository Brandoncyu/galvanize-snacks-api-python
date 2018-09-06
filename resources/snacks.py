import sqlite3
from flask_restful import Resource, reqparse
from models.snacks import SnacksModel
import random

class Snacks(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str
    )
    parser.add_argument('description',
        type=str
    )
    parser.add_argument('price',
        type=int
    )
    parser.add_argument('img',
        type=str
    )
    parser.add_argument('is_perishable',
        type=bool
    )

    def get (self, id):
        snacks = SnacksModel.find_by_id(id)
        if snacks:
            return {'data': snacks.json()}, 201
        return {'message': 'Snack with provided ID is not found'}, 404

    def patch(self, id):
        data = Snacks.parser.parse_args()
        snack = SnacksModel.find_by_id(id)
        if snack:
            if data['name']:
                snack.name = data['name']
            if data['description']:
                snack.description = data['description']
            if data['price']:
                snack.price = data['price']
            if data['img']:
                snack.img = data['img']
            if data['is_perishable'] == True:
                snack.is_perishable = True
            elif data['is_perishable'] == False:
                snack.is_perishable = False
        else:
            return {'message': 'item does not exist'}, 400


        snack.save_to_db()

        return {'data': snack.json()}, 200

    def delete(self, id):
        snacks = SnacksModel.find_by_id(id)
        if snacks:
            snacks.delete_from_db()

        return {'message': 'Snack Deleted'}, 202

class SnackList(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('name',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('description',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('price',
        type=int
    )
    parser.add_argument('img',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    parser.add_argument('is_perishable',
        type=bool,
        required=True,
        help="This field cannot be left blank!"
    )

    def get(self):
        return {'data': [snacks.json() for snacks in SnacksModel.query.all()]}

    def post(self):
        data = SnackList.parser.parse_args()
        snack = SnacksModel(data['name'], data['description'], data['price'], data['img'], data['is_perishable'])
        snack.save_to_db()

        return {'data': snack.json()}, 201

class SnackFeatured(Resource):
    def get(self):
        snacks = list(SnacksModel.query.all())
        length = len(snacks) - 1
        num1 = random.randint(0, length)
        num2 = random.randint(0, length)
        num3 = random.randint(0, length)

        return {'data': [ snacks[num1].json2(), snacks[num2].json2(), snacks[num3].json2() ]}
