from flask import Flask, redirect, request

app = Flask(__name__)

@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(redirect_for(request.headers, path), code=302)

def redirect_for(headers, path):
    return 'https://ip.sb/ip/{ip}'.format(ip=headers.get('x-forwarded-for'))
