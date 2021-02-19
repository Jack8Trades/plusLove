import flask
from random import randint
from flask import request, jsonify

app = flask.Flask(__name__)
app.config["DEBUG"] = True

pickupLines= [
    {
       "pickupLine": "You are cute!"
    }
   
]





def populateAPI():
     i = 0
     file = open("pickuplines.txt", "r")
     for line in file:
         object = {
             "pickupLine": line
         }
         pickupLines.append(object)
     file.close()

@app.route('/', methods=['GET'])
def home():
    return "sjfdhsfhjskd"




@app.route('/randomQuote' ,  methods=['GET'])
def getRandomQuote():
    populateAPI()
    randomNumber = randint(0, 250)
    return jsonify(pickupLines[randomNumber])

app.run()
