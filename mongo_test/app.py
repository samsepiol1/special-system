from flask_pymongo import PyMongo
import flask
from geopy import Nominatim
import urllib
import json
import requests

app = flask.Flask("app")

app.config["MONGO_URI"] = "mongodb://localhost:27017/coordinate_city"
mongodb_client = PyMongo(app)
db = mongodb_client.db

@app.route("/add_one")
def add_one():
    i = 0
    urlData = "http://localhost:3007/api/v1/bairros/"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    JSON_object = json.loads(data.decode('utf-8'))
    for i in range(len(JSON_object)):
         rua = JSON_object[i]['rua']
         bairro = JSON_object[i]['nome_bairro']
         geolocator = Nominatim(user_agent="steve.jkl5@gamil.com")
         location = geolocator.geocode(str(rua) + " " + str(bairro) + " " + "Parnamirim")
         if rua == None and bairro == None:
             print("Not Found Adress")
         elif location.latitude == None and location.longidute == None:
            print('Data Not Found')
         else:
            #obj = {'lat': location.latitude, 'long': location.longitude}
            #x = requests.post(urlData, data=obj)
            db.todos.insert_one({'lat': location.latitude, 'long': location.longitude})

            try:
                print(location.latitude, location.longitude)
                return flask.jsonify(message="success")
            except AttributeError:
                print("Endereço não encontrado")
                print("Don't save")



@app.route("/add_many")
def add_many():
    i = 0
    urlData = "http://localhost:3007/api/v1/bairros/"
    webURL = urllib.request.urlopen(urlData)
    data = webURL.read()
    JSON_object = json.loads(data.decode('utf-8'))
    for i in range(len(JSON_object)):
         rua = JSON_object[i]['rua']
         bairro = JSON_object[i]['nome_bairro']
         geolocator = Nominatim(user_agent="steve.jkl5@gamil.com")
         location = geolocator.geocode(str(rua) + " " + str(bairro) + " " + "Parnamirim")
         if rua == None and bairro == None:
             print("Not Found Adress")
         elif location.latitude == None and location.longidute == None:
            print('Data Not Found')
         else:
            obj = {'lat': location.latitude, 'long': location.longitude}
            #x = requests.put(urlData, data=obj)
            db.todos.insert_many([{'lat': location.latitude, 'long': location.longitude}])
            try:
                print(location.latitude, location.longitude)
                return flask.jsonify(message="success")
            except AttributeError:
                print("Endereço não encontrado")
                print("Don't save")
   

