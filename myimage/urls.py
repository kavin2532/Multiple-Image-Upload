'''
Created on 28-Apr-2021

@author: KAVIN MADHAIYAN
'''
from django.urls import path
from . import views
from image.urls import urlpatterns
urlpatterns=[
    path('image/',
        views.uploadeMulipleView,name="upload-multiple"),
]