import petname
from flask import Flask, render_template, make_response

app = Flask(__name__)


@app.route('/')
def index():
    pet = petname.generate()
    resp = make_response(render_template("/animal.html", pet=pet))
    return resp
