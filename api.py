import os, os.path, sqlite3
from flask import Flask, g, jsonify

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')
DATABASE = os.path.join(os.getenv('OPENSHIFT_DATA_DIR'), 'tweets.db')
INCLUDE_RETWEETS = False

@app.before_request
def before_request():
    g.db = sqlite3.connect(DATABASE)


@app.route("/tweets")
def hello():
    tweets = g.db.execute("SELECT text, user, time, name, retweet_status FROM tweet").fetchall()
    return jsonify(tweets)


# @app.route('/<path:resource>')
# def serveStaticResource(resource):
#     return send_from_directory('static/', resource)
#
# @app.route("/test")
# def test():
#     return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run(debug=True)
