from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^items/$', views.ItemList.as_view()),
]
