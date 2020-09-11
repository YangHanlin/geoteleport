from flask import Flask, redirect, request
import sys

sys.path.insert(0, '..')
from lib import redirection_provider

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(redirection_provider.redirect(request.headers, path), code=302)
