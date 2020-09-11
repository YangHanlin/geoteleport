import geoip2.database

def redirect(headers, path):
    return 'https://ip.sb/ip/{ip}'.format(ip=headers.get('x-forwarded-for'))
