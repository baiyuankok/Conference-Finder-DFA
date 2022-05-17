from django.urls import re_path
from .views import indexView

urlpatterns = [
    re_path(r'^$', indexView, name='index')
]