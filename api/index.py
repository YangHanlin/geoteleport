from flask import Flask, redirect
from lib import redirection_provider

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(f'https://domestic.pages.tree-diagram.site/{path}', code=302)
