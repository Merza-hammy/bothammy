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
  crypto_name = data['conversation']['memory']['crypto']['raw']

  # FETCH BTC/USD/EUR PRICES
  r = requests.get("https://min-api.cryptocompare.com/data/price?fsym="+crypto_name+"&tsyms=BTC,USD,EUR")

  return jsonify(
    status=200,
    replies=[{
      'type': 'text',
      'content': 'El precio de el %s es %f BTC y %f USD' % (crypto_name, r.json()['BTC'], r.json()['USD'])
   }]
  )

@app.route('/errors', methods=['POST'])
def errors():
  print(json.loads(request.get_data()))
  return jsonify(status=200)

app.run(port=port, host="0.0.0.0")
