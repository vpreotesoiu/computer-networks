from flask import Flask, jsonify
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return "Vlad Preotesoiu (numar matricol 349/2024)"

'''
This method expects a json content.
Use header: 'Content-Type: application/json'
'''
@app.route('/post', methods=['POST'])
def post_method():
    print("Got from user: ", request.get_json())
    print(request.get_json()['value']*2)
    return jsonify({'got_it': 'yes'})

@app.route('/item/<num>')
def item_method(num):
    return jsonify({'item': num})

@app.route('/ip')
def ip_method():
    return jsonify({'ip': request.host.split(':')[0]})

@app.route('/subnetmask', methods=['POST'])
def subnetmask_method():
    pass

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
