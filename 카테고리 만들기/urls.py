from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('<int:post_id>/', views.post_detail, name='post_detail'),
    path('search/', views.search, name='search'),
    path('category/<str:slug>/', views.category_page )
]
