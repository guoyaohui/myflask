from flask import Flask
from flask.ext.script import Manager

app = Flask(__name__)

manager = Manager(app)


@app.route('/')
def index():
     return '<h1>Hello World!Hello eveH<h1>'

@app.route('/user/<name>')
def user(name):
     return '<h2>Hello Spring %s !<h2>' % name

if __name__ == '__main__':
     manager.run()
