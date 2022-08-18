from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:post_id>', views.post_detail, name='post_detail'),
    path('search', views.search, name='search')
]
