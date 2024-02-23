from flask import Flask, request, jsonify
from openai import OpenAI
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

client = OpenAI(
    api_key='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', )


@app.route('/')
def index():

  return jsonify({"msg": "Hello home"})


@app.route('/generate', methods=['POST'])
def generate():
  data = request.get_json()
  print(data["prompt"])
  response = client.images.generate(
      model="dall-e-3",
      prompt=data["prompt"],
      size="1792x1024",
      quality="standard",
      n=1,
  )

  image_url = response.data[0].url
  print(image_url)
  print(type(image_url))
  return jsonify({"imageUrl": image_url})


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=80)
