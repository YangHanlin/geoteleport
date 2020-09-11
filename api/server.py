from flask import Flask, redirect

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def redirect(path):
    return redirect(f'https://domestic.pages.tree-diagram.site/{path}', code=302)
