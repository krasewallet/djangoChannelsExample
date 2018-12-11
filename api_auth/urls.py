from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.settings import api_settings
from rest_framework.routers import DefaultRouter
from . import views
app_name = 'api_auth'
urlpatterns  = [
    path('photos/', views.photos),
]
