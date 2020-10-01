import requests
from flask import Flask
from app.merge import merge

app = Flask(__name__)


@app.route("/")
def index():
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return ('<pre> Teapot: ' + r.text + '</pre>')


@app.route("/merge")
def help():
    return ('<h2>This will run the merge code.</h2>')
