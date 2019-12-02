import ise.connection as connection
import ise.exceptions as exceptions
import ise.endpoints as endpoints

class Ise(object):
    def __init__(self, host, **kwargs):
        self.connection = connection.IseConnection(host=host, **kwargs)
        self.exceptions = exceptions
        self.endpoints = endpoints.Endpoints(self.connection)