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
    req = request.get_json()
    ip = req['ip']
    nodes = int(req['noduri'])
    bdcast_nw_offset = -2
    host_bits = 0
    while 2**host_bits + bdcast_nw_offset < nodes:
        host_bits += 1
    cidr = 32-host_bits
    mask = ['1' for i in range(cidr)] + ['0' for i in range(32-cidr)]
    mask_with_split_bytes = '.'.join([str(int(''.join(mask[i:i+8]),2)) for i in range(0,32,8)])
    return jsonify({'output':mask_with_split_bytes})

@app.route('/<name>')
def hello_name(name):
    return "Hello {}!".format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8001)
