from flask import Flask, redirect, abort, request
import geoip2.database
import pathlib
import json
import os

app = Flask(__name__)
base_path = str(pathlib.Path(__file__).parent.parent.absolute())


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    try:
        return redirect(redirect_for(request.headers, path), code=302)
    except RuntimeError as e:
        abort(400, str(e.args))


def redirect_for(headers, path):
    ip = headers.get('x-forwarded-for')
    scheme = headers.get('x-forwarded-proto')
    config = load_config(base_path + os.getenv('CONFIG_PATH'))
    rules, fallback = config[:-1], config[-1]
    with geoip2.database.Reader(base_path + os.getenv('GEOIP_DB_PATH')) as reader:
        region = reader.country(ip).country.iso_code
    for rule in rules:
        if region in rule['regions']:
            return rule['redirect'].format(scheme=scheme, path=path)
    return fallback['redirect'].format(scheme=scheme, path=path)


def load_config(config_path):
    return json.load(open(config_path, 'r', encoding='utf-8'))
