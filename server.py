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

  # FETCH THE CRYPTO NAME
  city = data['conversation']['memory']['location']['value']

  # FETCH BTC/USD/EUR PRICES
  r = requests.get("https://api.apixu.com/v1/current.json?key=9a48c907e1534875947150810181312&q="+city)

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

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")
