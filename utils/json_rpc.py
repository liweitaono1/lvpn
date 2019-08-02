import random
import requests
import json

from requests import HTTPError

from lvpn.settings import SERVER_API_URL, X_VPNADMIN_HUBNAME, X_VPNADMIN_PASSWORD


class SoftetherAPIException(Exception):
    """ generic Softether api exception
    code list:
         -32602 - Invalid params (eg already exists)
         -32500 - no permissions
    """
    pass


class SoftetherAPI():
    def __init__(self,
                 hubname=None,
                 password=None,
                 server=SERVER_API_URL,
                 session=None,
                 timeout=None):
        self.session = session if session else requests.Session()
        self.session.headers.update({
            'Content-Type': 'application/json-rpc',
            'Cache-Control': 'no-cache',
            'X-VPNADMIN-HUBNAME': hubname if hubname else X_VPNADMIN_HUBNAME,
            'X-VPNADMIN-PASSWORD': password if password else X_VPNADMIN_PASSWORD
        })
        self.url = server + 'api/' if server.endswith('/') else server + '/api/'
        self.timeout = timeout

    def test(self):
        pass

    def do_request(self, method, params=None):
        # id = "".join(random.choice("0123456789") for _ in range(15))
        self.request_json = {
            "jsonrpc": "2.0",
            # "id": id,
            "method": method,
            'params': params or {},
        }

        response = self.session.post(
            self.url,
            data=json.dumps(self.request_json),
            timeout=self.timeout,
            verify=False
        )
        try:
            response.raise_for_status()
        except HTTPError as e:
            print(e)
            return {'error': 'API认证失败，请联系开发人员！！！'}
        if not len(response.text):
            raise SoftetherAPIException("Received empty response")
        try:
            response_json = json.loads(response.text)
            # if response_json['id'] == id:
            #     pass

        except ValueError:
            return "Unable to parse json: %s" % response.text
        if 'error' in response_json:
            return response_json
        return response_json['result']

    def __getattr__(self, attr):
        """Dynamically create an object class (ie: host)"""

        def fn(*args, **kwargs):
            if args and kwargs:
                raise TypeError("Found both args and kwargs")
            return self.do_request(
                attr,
                args or kwargs
            )

        return fn


if __name__ == '__main__':
    resp = requests.post(
        SERVER_API_URL,
        data=json.dumps({
            "jsonrpc": "2.0",
            "id": "123456789",
            "method": "GetServerInfo",
            "params": {
            }
        }),
        headers={
            'X-VPNADMIN-HUBNAME': X_VPNADMIN_HUBNAME,
            'X-VPNADMIN-PASSWORD': X_VPNADMIN_PASSWORD
        },
        verify=False)
    print(resp.text)
