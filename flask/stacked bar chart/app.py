from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
import random
from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format

    data = []
    Positive = random.sample(range(0,100),5)
    Neutral = random.sample(range(0,100),5)
    Negative = random.sample(range(0,100),5)

    data = [Positive,Neutral, Negative]


    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(debug=True)
