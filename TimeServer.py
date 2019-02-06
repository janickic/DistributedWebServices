import os, sys, time
from TimeServer_client import *
from ZSI.twisted.wsgi import (SOAPApplication,
                              soapmethod,
                              SOAPHandlerChainFactory)

class TimeService(SOAPApplication):
    factory = SOAPHandlerChainFactory
    wsdl_content = dict(name='Time', 
                        targetNamespace='urn:Time', 
                        imports=(), 
                        portType='',
                        )

    def __call__(self, env, start_response):
        self.env = env
        return SOAPApplication.__call__(self, env, start_response)

    @soapmethod(TimeRequest.typecode, 
                TimeResponse.typecode, 
                operation='Time', 
                soapaction='Time')
    def soap_Time(self, request, response, **kw):
        # Return server time
        now = time.time()
        print "Current time on server:", now
        response._value = now
        return request, response

def main():
    from wsgiref.simple_server import make_server
    from ZSI.twisted.wsgi import WSGIApplication


    application         = WSGIApplication()
    httpd               = make_server('', 7000, application)
    application['Time'] = TimeService()
    print "listening..."
    httpd.serve_forever()

if __name__ == '__main__':
    main()