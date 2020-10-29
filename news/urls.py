from django.urls import path
from .views import *

urlpatterns = [
    path('', news_list, name='news_list_url'),
    path('detail/<str:slug>/', NewsDetail.as_view(), name='new_detail_url'),
    path('tags/', tags_list, name='tag_list_url'),
    path('tag/create', TagCreate.as_view(), name='tag_create_url'),
    path('tag/<str:slug>/', TagsDetail.as_view(), name='tag_detail_url'),

]