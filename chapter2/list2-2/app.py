from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return "welcome to flask world"


if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
