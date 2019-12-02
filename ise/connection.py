import requests, json
from ise import exceptions

class IseConnection(object):
    def __init__(self, ssl_verify=False, use_ssl=True, host=None, auth=None, port='9060', api_prefix=None):

        self.use_ssl = use_ssl
        self.host = host
        self.port = port
        self.auth = auth
        self.api_prefix = api_prefix

        self.base_url = 'http{s}://{host}{p}{prefix}'.format(s='s' if use_ssl else '', p=':{}'.format(self.port) if self.port else '', host=self.host, prefix='/ers/sdk' if api_prefix is None else api_prefix)

        self.session = requests.Session()
        self.session.verify = ssl_verify

    def __request():
        pass

    def get():
        pass

    def put():
        pass

    def patch():
        pass

    def post():
        pass

    def delete():
        pass

    def close():
        pass