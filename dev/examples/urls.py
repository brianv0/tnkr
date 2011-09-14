from django.conf.urls.defaults import *
from jsonrpc import jsonrpc_site
import views

urlpatterns = patterns('',
    (r'^$', 'examples.views.index'),
    (r'^json/', jsonrpc_site.dispatch),
    (r'^hello/', include('examples.hello.urls')),
)
