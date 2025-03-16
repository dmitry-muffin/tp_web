# myproject/urls.py
from django.contrib import admin
from django.urls import path
from tp_web_app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('index_na', index_na, name='index_na'),
    path('ask', ask, name='ask')
]
