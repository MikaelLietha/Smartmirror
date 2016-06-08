#from django.conf.urls import url
#from  polls import views
from Smartmirror.urls import url

from . import views

urlpatterns = [
	url(r'^$',views.index, name="index"),
	url(r'^something/', views.something),
	]