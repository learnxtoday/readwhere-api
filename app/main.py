import requests
from flask import Flask

app = Flask(__name__)


@app.route("/")
def index():
    r = requests.get('http://httpbin.org/status/418')
    print(r.text)
    return ('<pre>' + r.text + '</pre>')
