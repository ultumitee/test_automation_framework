import os
import sys

from requests.auth import HTTPBasicAuth
from requests.adapters import HTTPAdapter
import requests


class RequestEngine(object):
    def request_sender(self,url_link,request_type,params=None,headers=None,body_params=None):
        """Sending the required request with changing the max retry value.
                # url_link = URL link to use for gathering data
                # request_type = GET for default. state if different than GET
                # body_param = requested when POST is used, otherwise no needed
                """
        response=""
        adapter = HTTPAdapter(max_retries=5)
        session = requests.Session()
        session.mount(url_link, adapter)
        try:
            if request_type == "GET":
                response = session.get(url=url_link,params=params,headers=headers)
            elif request_type == "POST":
                response = session.post(url=url_link,data=body_params,headers=headers,params=params)
            elif request_type == "PUT":
                response = session.put(url=url_link,data=body_params,headers=headers,params=params)
            return response
        except ConnectionError as e:
            print(e)
            os._exit(1)