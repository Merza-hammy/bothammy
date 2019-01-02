# coding=utf-8
from flask import Flask, request, jsonify
import json
import requests
import objectpath
import os
 
app = Flask(__name__)
port = int(os.environ["PORT"]) #definicion de puerto de salida
 
#@app.route('/', methods=['POST'])

#def index():
  
                #postRece = json.loads(request.get_data())
                #intent = str(postRece['nlp']['sumar'][0]['slug']) #Se obtiene el nombre del intent desde el post de Recast
                #skill = str(postRece['conversation']['suma']) #Se obtiene el nombre del skill desde el post de Recast
                #print(skill)
                #print(intent)
                if intent == "sumar" and skill == "suma": #Si el intent y el skill es el esperado
                                              
                a=float
                b=float
               suma= a+b
               print(str(suma))

               
               
               

 
#cf login
#API Endpoint:https://api.cf.eu10.hana.ondemand.com
#cf push botRecast manifest file C:\Users\i861443\Desktop\python SCP\Recast\manifest.yml
#requirements.txt para instalación de imports

