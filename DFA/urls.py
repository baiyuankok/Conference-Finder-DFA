from django.urls import re_path, path
from .views import indexView, processDFA

urlpatterns = [
    path('', indexView, name='index'),
    path('result/', processDFA, name="process_DFA")
]