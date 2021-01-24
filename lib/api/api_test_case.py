from lib.api.request_engine import RequestEngine

class APITestCase(object):
    API_ROOT="https://600db55c3bb1d100179de2e6.mockapi.io/api/"
    request_engine= RequestEngine()
    def get_books(self):
        url=self.API_ROOT+"books"
        response=self.request_engine.request_sender(url_link=url,request_type="GET")
        return response

    def put_a_book(self,params):
        url=self.API_ROOT+"books"
        response=self.request_engine.request_sender(url_link=url,params=params,request_type="PUT")
        return response
    def get_a_book(self,id):
        url=self.API_ROOT+"books/{}".format(id)
        response=self.request_engine.request_sender(url_link=url,request_type="GET")
        return response

