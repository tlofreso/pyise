import ise.connection as connection
import ise.exceptions as exceptions

class ise(object):
    def __init__(self, host, **kwargs):
        self.connection = connection.iseconnection(host=host, **kwargs)
        self.exceptions = exceptions