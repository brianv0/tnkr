from django.conf.urls.defaults import *
from jsonrpc import jsonrpc_site
import rpc

urlpatterns = patterns('',
    (r'', jsonrpc_site.dispatch),
)
