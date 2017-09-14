from django.conf.urls import url
from App2 import views

urlpatterns = [
    url(r'^$',views.help,name='help'),
]
