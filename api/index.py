from flask import Flask, redirect, request
import geoip2.database
import pathlib

app = Flask(__name__)


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return redirect(redirect_for(request.headers, path), code=302)


def redirect_for(headers, path):
    ip = headers.get('x-forwarded-for')
    app.logger.info('IP = %s', ip)
    scheme = 'https'
    domestic_base = '{scheme}://domestic.pages.tree-diagram.site/{path}'
    global_base = '{scheme}://global.pages.tree-diagram.site/'
    with geoip2.database.Reader(str(pathlib.Path(__file__).parent.parent.absolute()) + '/db/Country.mmdb') as reader:
        response = reader.country(ip)
        app.logger.info('country or region = %s', response.country.iso_code)
        if response.country.iso_code == 'CN':
            return domestic_base.format(scheme=scheme, path=path)
        else:
            return global_base.format(scheme=scheme, path=path)
