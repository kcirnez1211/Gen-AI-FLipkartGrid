from flask import Flask, jsonify

import openai
import os
from flask import render_template

my_secret = os.environ['OPENAI_KEY']
openai.api_key =my_secret

app = Flask(__name__)


@app.route('/')
def index():
  return render_template('index.html', )
  
@app.route('/generateimages/<prompt>')
def generate(prompt):
  print("prompt:", prompt)
  response = openai.Image.create(prompt=prompt, n=2, size="256x256") 
  print(response)
  return jsonify(response)


app.run(host='0.0.0.0', port=81)
