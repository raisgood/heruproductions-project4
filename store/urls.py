from django.urls import path
from . import store_views

urlpatterns = [
    path('', store_views.index, name='index'),
    path('store/', store_views, name='store'),
]