from django import http
import logging
from jsonrpc import jsonrpc_method

logging.basicConfig(filename="/tmp/json.log",
                    level=logging.DEBUG)

logging.debug("Basic views loaded")


def index(request):
    r = http.HttpResponse('<h1>Django examples</h1><ul>')
    r.write('<li><a href="hello/html/">Hello world2 (HTML)</a></li>')
    r.write('<li><a href="hello/text/">Hello world (text)</a></li>')
    r.write('<li><a href="hello/write/">HttpResponse objects are file-like objects</a></li>')
    r.write('<li><a href="hello/metadata/">Displaying request metadata</a></li>')
    r.write('<li><a href="hello/getdata/">Displaying GET data</a></li>')
    r.write('<li><a href="hello/postdata/">Displaying POST data</a></li>')
    r.write('</ul>')
    return r


@jsonrpc_method('sayHello')
def whats_the_time(request, name='Lester'):
    logging.debug('whats_the_time called with name %s' %name)
    return "Hello %s" % name
  
@jsonrpc_method('gimmeThat')
def something_special(request, secret_data=False):
    if 'user' in secret_data:
	if 'verb' in secret_data:
	    return '%s %s' %(secret_data['user'],secret_data['verb'])
    return {'sauce': ['authenticated', 'sauce']}

@jsonrpc_method('test2')
def tryAgain(request, data='aaa'):
    return 'this %s' %data
