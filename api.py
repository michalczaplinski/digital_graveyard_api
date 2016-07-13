import os, os.path, sqlite3, json
from flask import Flask, g, jsonify

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
DATABASE = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'tweets.db')
INCLUDE_RETWEETS = False

@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)


@app.route("/db")
def tweets():
    tweets = g.db.execute("SELECT text, user, time, name, retweet_status FROM tweet").fetchall()
    return jsonify(tweets)

@app.route("/file")
def tweets_from_file():
    tweets_file = open(os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'tweets.json'), 'r')
    tweets = json.load(tweets_file)
    return jsonify(tweets)


if __name__ == '__main__':
    app.run(debug=True)
