from django.conf.urls import url
from . import views

app_name = "sistemaExperto"

urlpatterns = [
    #/music/
    # the name here is the function in views
    url(r'^$', views.buscar , name='buscar'),
    ]
