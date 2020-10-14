from django.urls import path, include
from .views import PostList, PostDetail, UserList, UserDetail, PaperList, PaperDetail, ApiRoot
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('', ApiRoot.as_view(), name="root"),
    path('papers/', PaperList.as_view(), name="papers"),
    path('papers/<int:pk>/', PaperDetail.as_view(), name="single-paper"),
    path('users/', PostList.as_view(), name="users"),
    path('users/<int:pk>/', PostDetail.as_view(), name="single-user"),
    path('posts/', PostList.as_view(), name="posts"),
    path('posts/<int:pk>/', PostDetail.as_view(), name="single-post"),
]
urlpatterns = format_suffix_patterns(urlpatterns)
