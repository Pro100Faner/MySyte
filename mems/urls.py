from django.urls import path
from .views import *

urlpatterns = [
    path('', mems_list, name='mem_list_urls'),
    path('detail/<str:slug>/', MemsDetail.as_view(), name='mem_detail_url'),
    path('create/', MemCreate.as_view(), name='mem_create_url'),
]