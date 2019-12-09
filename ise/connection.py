import requests, json, socket
from requests.auth import HTTPBasicAuth
from ise import exceptions


class IseConnection(object):
    def __init__(
        self,
        ssl_verify=False,
        use_ssl=True,
        host=None,
        auth=None,
        user=None,
        password=None,
        port="9060",
        api_prefix=None,
    ):

        self.use_ssl = use_ssl
        self.host = host
        self.port = port
        self.auth = auth
        self.user = user
        self.password = password
        self.api_prefix = api_prefix

        self.base_url = "http{s}://{host}{p}{prefix}".format(
            s="s" if use_ssl else "",
            p=":{}".format(self.port) if self.port else "",
            host=self.host,
            prefix="/ers/config" if api_prefix is None else api_prefix,
        )

        self.session = requests.Session()
        self.session.verify = ssl_verify

        self.session.auth = HTTPBasicAuth(user, password)

        self.session.headers.update({"Content-type": "application/json"})
        self.session.headers.update({"Accept": "application/json"})

    def __request(self, method, params=None, body=None, url=None):

        if url is None:
            url = self.base_url + str(params)

        request = requests.Request(method=method, url=url, json=body)
        prepared_request = self.session.prepare_request(request)

        try:
            response = self.session.send(prepared_request)
        except socket.gaierror:
            err_msg = "Unable to find address: {}".format(self.host)
            raise socket.gaierror(err_msg)
        except requests.exceptions.ConnectionError:
            err_msg = "Unable to connect to ISE host: {}".format(self.host)
            raise ConnectionError(err_msg)
        except requests.exceptions.Timeout:
            raise TimeoutError("Connection to ISE host timed out")
        except Exception as e:
            raise Exception(e)
        finally:
            self.close()

        try:
            response_data = response.json()
        except:
            response_data = response.content

        return response.ok, response.status_code, response_data

    def get(self, params, **kwargs):

        url = "{}{}".format(self.base_url, params)

        resp_ok, resp_status, resp_data = self.__request("GET", params=params, url=url)

        if resp_ok and resp_status == 200:
            if "results" in resp_data:
                return resp_data["results"]
            else:
                return resp_data
        else:
            return []

    def put(self, params, **kwargs):

        url = "{}{}".format(self.base_url, params)

        resp_ok, resp_status, resp_data = self.__request("PUT", params=params, data=data, url=url)

    def patch():
        pass

    def post():
        pass

    def delete():
        pass

    def close(self):

        self.session.close()
