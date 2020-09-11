from flask import Flask, redirect, request
# from api import redirection_provider
import reflection_provider

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(redirection_provider.redirect(request.headers, path), code=302)
