from django.urls import path
from .views import ArticleListCreateAPIView, ArticleDetailAPIView, CommentListCreateAPIView, CommentDetailAPIView

urlpatterns = [
    path("articles/", ArticleListCreateAPIView.as_view(), name="article_list_create"),
    path("articles/<int:pk>/", ArticleDetailAPIView.as_view(), name="article_detail"),
    path("comments/", CommentListCreateAPIView.as_view(), name="comment_list_create"),
    path("comments/<int:pk>/", CommentDetailAPIView.as_view(), name="comment_detail"),]