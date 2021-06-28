from typing import NamedTuple
from flask import Flask
app = Flask(NamedTuple)
@app.route('/')
def index():
 return '<h1>Hello</h1>'