from django.conf.urls.defaults import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

from . import views

urlpatterns = [ 
	url(r'^polls/', include('polls.urls')),
	url(r'^admin/', admin.site.urls),
    url(r'^Test/', views.Test),
    url(r'^$', views.index, name="index"),
	]
	#patterns('',
    # Examples:
    # url(r'^$', 'Smartmirror.views.home', name='home'),
    # url(r'^Smartmirror/', include('Smartmirror.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
	#)
