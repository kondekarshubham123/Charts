from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
import time
from random import random
from flask import Flask, render_template, make_response
app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')

@app.route('/dataPiecha', methods=["GET", "POST"])
def dataPie():
    # Data Format
    # [Positive, Netural, Negative]

    Positive = random() * 100
    Netural = random() * 55
    Negative = random() * 67

    data = [Positive, Netural, Negative]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Positive, Netural, Negative]

    Positive = random() * 100
    Netural = random() * 55
    Negative = random() * 67

    data = [time.mktime(time.gmtime()) * 1000, Positive, Netural, Negative]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

@app.route('/words', methods=["GET", "POST"])
def wordsdata():

    data = "My Name is Shubsdfghjkwhdc wudiwuddad ksd ham Kondekar Kondekar Kondekar"
    data+=' Kondekar'

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response

if __name__ == "__main__":
    app.run(debug=True)
