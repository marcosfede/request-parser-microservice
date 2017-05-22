from flask import Flask, request, jsonify
from os import environ
app = Flask(__name__)


@app.route('/')
def hello_world():
    return jsonify({
        'ip': request.remote_addr or "unkown",
        'language': request.accept_languages[0][0] or "unkown",
        'os': request.user_agent.platform or "unknown"
    })


if __name__ == '__main__':
    app.run(environ.get('PORT'))
