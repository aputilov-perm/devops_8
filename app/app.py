from flask import Flask, request, jsonify
from calculator import add, subtract

app = Flask(__name__)

@app.route('/add')
def do_add():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = add(a, b)
    return jsonify(result=result)

@app.route('/subtract')
def do_subtract():
    a = int(request.args.get('a'))
    b = int(request.args.get('b'))
    result = subtract(a, b)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
