import flask
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

pickupLines= [
    {'id': 0,
     'saying':"You are pretty"
     },
     {'id': 1,
     'saying':"You are amazing"
     }
    ]


@app.route('/', methods=['GET'])
def home():
    return "sjfdhsfhjskd"




@app.route('/randomQuote' ,  methods=['GET'])
def getRandomQuote():
    
    return jsonify(pickupLines[0])

app.run()
