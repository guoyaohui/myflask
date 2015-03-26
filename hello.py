from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
     return '<h1>Hello World!\nHello Liuying<h1>'

@app.route('/user/<name>')
def user(name):
     return '<h2>Hello Spring %s !<h2>' % name

if __name__ == '__main__':
     app.run(debug = True)
