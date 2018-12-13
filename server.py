from flask import Flask, request, jsonify
import json
import requests
import os

app = Flask(__name__)
port = int(os.environ["PORT"])
print(port)

@app.route('/', methods=['POST'])
def index():
  print(port)
  data = json.loads(request.get_data()) 

    #Get City
    city = data['nlp']['entities']['location'][0]['raw']
    #Fetch Weather Data
    r = requests.get("https://api.apixu.com/v1/current.json?key=<9a48c907e1534875947150810181312>&q="+city)

    return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'La temperatura en %s, %s es de %d °C. Hay vientos de %d kmh y humedad del %d %%'
       % (r.json()['location']['name'], r.json()['location']['country'],
       r.json()['current']['temp_c'], r.json()['current']['wind_kph'],
       r.json()['current']['humidity']),
    }]
  )
port = os.getenv('PORT', 8080)
if __name__ == '__main__':
    app.debug = not os.getenv('PORT')
    app.run(host='0.0.0.0', port=int(port))
