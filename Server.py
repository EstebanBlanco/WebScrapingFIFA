from flask import Flask, jsonify
import DatabaseManager


app = Flask(__name__)

def make_response(result):
    response = jsonify(result[0])
    response.status_code = result[1]
    return response

@app.route('/', methods=['GET','POST'])
def hello_world():
  return 'Hello Worlds!'

# GETs
@app.route('/getData', methods=['GET','POST'])
def getData():
    return make_response(DatabaseManager.SelectData())

if __name__ == '__main__':
    app.run(host='0.0.0.0')
