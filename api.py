from flask import Flask, redirect, jsonify, make_response
import requests

app = Flask(__name__)


@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'Error': 'Bad request'}), 400)


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'Error': 'Not found'}), 404)


@app.route('/gif/cute', methods=['GET'])
def get_cute_gif():
    r = requests.get('https://evergene.io/api/hug')
    return redirect(r.json()['url'], code=302)


if __name__ == '__main__':
    app.run()
