import os, os.path, sqlite3, json
from flask import Flask, g, jsonify
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

app.config.from_pyfile('flaskapp.cfg')
DATABASE = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'tweets.db')
INCLUDE_RETWEETS = False

@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)

class Db(Resource):
    def get(self):
        tweets = g.db.execute("SELECT text, user, time, name, retweet_status FROM tweet").fetchall()
        return jsonify(tweets)

class File(Resource):
    def get(self):
        tweets_file = open(os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'tweets.json'), 'r')
        tweets = json.load(tweets_file)
        return jsonify(tweets)

api.add_resource(Db, '/db')
api.add_resource(File, '/file')

if __name__ == '__main__':
    app.run(debug=True)
