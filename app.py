from flask import Flask, jsonify

app = Flask(__name__)

#headers = {'ContentType':'application/json'}

@app.route('/', methods=['GET'])
def get_products():
  #return jsonify({'msg':'Hello world'}), 200, headers
  return jsonify({'msg':'Hello world'}), 200

if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0')
