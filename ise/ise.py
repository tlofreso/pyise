import ise.connection as connection
import ise.exceptions as exceptions

class Ise(object):
    def __init__(self, host, **kwargs):
        self.connection = connection.IseConnection(host=host, **kwargs)
        self.exceptions = exceptions