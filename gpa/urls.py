from django.conf.urls import url, include

import views

urlpatterns = [
    url('', views.index, name='index'),
]