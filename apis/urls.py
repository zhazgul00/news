from django.urls import path
from .views import ArticleListCreateAPIView, ArticleDetailAPIView, CommentListCreateAPIView, CommentDetailAPIView, CustomTokenObtainPairView, get_csrf_token
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('csrf-token/', get_csrf_token, name='csrf_token'),
    path("articles/", ArticleListCreateAPIView.as_view(), name="article_list_create"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail"),
    path("comments/", CommentListCreateAPIView.as_view(), name="comment_list_create"),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment_detail"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('custom-token/', CustomTokenObtainPairView.as_view(), name='custom_token_obtain_pair'),]