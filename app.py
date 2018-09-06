from flask import Flask
from flask_restful import Api
from flask_cors import CORS

from resources.snacks import Snacks, SnackList, SnackFeatured
from resources.reviews import Reviews, ReviewsList

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'secret'
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all() #will create tables unless they exist already

api.add_resource(Snacks, '/api/snacks/<int:id>', strict_slashes=False)
api.add_resource(SnackList, '/api/snacks', strict_slashes=False)
api.add_resource(SnackFeatured, '/api/snacks/featured', strict_slashes=False)
api.add_resource(Reviews, '/api/snacks/<int:snack_id>/reviews', strict_slashes=False)
api.add_resource(ReviewsList, '/api/snacks/<int:snack_id>/reviews/<int:rev_id>', strict_slashes=False)

if __name__ == '__main__':
    from db import db
    db.init_app(app)
    app.run(port=5000, debug=True)
