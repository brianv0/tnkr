from django import http
import logging
from jsonrpc import jsonrpc_method
import time

logging.basicConfig(filename="/tmp/json.log",
                    level=logging.DEBUG)

logging.debug("json is being loaded...")

def reqtimer(reqtime, inctime, timeout):
    if reqtime < timeout:
        time.sleep(inctime)
        reqtime = reqtime + inctime
        return(False,reqtime)
    else:
        return(True,reqtime)

@jsonrpc_method('index')
def index(request):
    reqtime = 0
    timeout = 5
    inctime = .2
    reqtimeout = False
    while not reqtimeout:
        (reqtimeout,reqtime) = reqtimer(reqtime,inctime,timeout)
    response = 'timeout'
    return response


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

@jsonrpc_method('gimmeExample')
def gimmedict(request):
    return {'user':'Fake User', 'verb':' is a fake user'}

@jsonrpc_method('test2')
def tryAgain(request, data='aaa'):
    return 'this %s' %data

@jsonrpc_method('callStack')
def getcallstack(request):
    f1 = {'sayHello':"name='lester'"}
    f2 = {'gimmeThat':"secret_data=False"}
    
    s = {}
    s.update(f1)
    s.update(f2)
    return s


@jsonrpc_method('geturl')
def getearl(request,a,b,c,d,e):
    logging.debug(a)
    logging.debug(b)
    logging.debug(c)
    logging.debug(d)
    logging.debug(e)
    logging.debug("done.")
    return(["http://www.success.com","success"])
