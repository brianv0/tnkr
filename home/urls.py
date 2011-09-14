from django.conf.urls.defaults import *
from django.contrib import admin
admin.autodiscover()

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', 'home.views.index'),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),
    (r'^comments/', include('django.contrib.comments.urls')), 
    (r'^posts/', include('basic.blog.urls')), 
#    (r'^admin/', include('django.contrib.admin.urls')), 
    (r'^admin/', include(admin.site.urls)), 
    # Uncomment the next line to enable the admin:
    (r'^blog/', include('basic.blog.urls')),
    (r'^comments/', include('django.contrib.comments.urls')),
)
