from flask import Flask
from flask import request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def hello():
    return 'Hello World! Привет!'

def main():
    app.run(host='0.0.0.0', port=8080)

if __name__ == '__main__':
    main()
