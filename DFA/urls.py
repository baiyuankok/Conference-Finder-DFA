from django.urls import re_path, path
from .views import indexView, processDFA

urlpatterns = [
    re_path(r'^$', indexView, name='index'),
    path('processDFA/', processDFA, name="process_DFA")
]