import webapp2
import json


class BaseRequest(webapp2.RequestHandler):

    def options(self, *args, **kwargs):
        self.response.headers['Content-Type'] = 'application/json'
        self.response.headers['Access-Control-Allow-Origin'] = self.request.headers['Origin']
        self.response.headers['Access-Control-Allow-Headers'] = ('Origin, X-Requested-With, '
                                                                 'x-http-method-override, '
                                                                 'Content-Type, Accept, '
                                                                 'authorization')
        self.response.headers['Access-Control-Allow-Methods'] = ('DELETE, GET, HEAD, OPTIONS, '
                                                                 'PATCH, POST, PUT')
        self.response.headers['Access-Control-Allow-Credentials'] = 'true'
        self.response.headers['Access-Control-Max-Age'] = '600'

    def response_write(self, response):
        self.response.headers.add_header('Access-Control-Allow-Origin', '*')
        self.response.headers['Content-Type'] = 'application/json'
        self.response.write(json.dumps(response))
