import os
from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('flaskapp.cfg')

@app.route('/hello')
def index():
    return 'hello'

# @app.route('/<path:resource>')
# def serveStaticResource(resource):
#     return send_from_directory('static/', resource)
#
# @app.route("/test")
# def test():
#     return "<strong>It's Alive!</strong>"

if __name__ == '__main__':
    app.run()
