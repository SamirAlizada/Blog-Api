from django.urls import path
from . import views

urlpatterns = [
    path('blogs/', views.BlogListCreateApiView.as_view()),
    path('blogs/<int:pk>', views.BlogDetailApiView.as_view()),

    path('users/', views.UserListCreateApiView.as_view()),
    path('users/<int:pk>', views.UserDetailApiView.as_view(), name='user_detail'),
]