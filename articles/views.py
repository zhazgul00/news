from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, FormView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy, reverse 
from .models import Article, Comment
from .forms import CommentForm
from django.views import View 
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListAPIView
from apis.serializers import ArticleSerializer

class CommentGet(DetailView):
    model = Article
    template_name = "article_detail.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = CommentForm()
        context["comments"] = self.object.comment_set.all()
        return context


class CommentPost(SingleObjectMixin, FormView):
    model = Article
    form_class = CommentForm
    template_name = "article_detail.html"
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().post(request, *args, **kwargs)
    
    def form_valid(self, form):
            comment = form.save(commit=False)
            comment.article = self.object
            form.instance.author = self.request.user
            
            parent_id = self.request.POST.get('parent')
            if parent_id:
                comment.parent_id = parent_id  
            comment.save()
            return super().form_valid(form)
    

    def get_success_url(self):
        article = self.get_object()
        return reverse("article_detail", kwargs={"pk": article.pk})
    

from django.core.exceptions import PermissionDenied
import logging

logger = logging.getLogger(__name__)

class CommentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    fields = ("comment",)
    template_name = "comments_edit.html"  

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.object.article.pk})


class CommentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = "comments_delete.html"  

    def test_func(self):
        comment = self.get_object()
        return comment.author == self.request.user

    def get_success_url(self):
        return reverse_lazy("article_detail", kwargs={"pk": self.object.article.pk})




class ArticleDetailView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        view = CommentGet.as_view()
        return view(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        view = CommentPost.as_view()
        return view(request, *args, **kwargs)

class ArticleCreateView(LoginRequiredMixin, CreateView):
    model = Article
    template_name = "article_new.html"
    fields = ("title", "body") 

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleListView(LoginRequiredMixin, ListView):
    model = Article
    template_name = "article_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['comments'] = {article.pk: article.comment_set.all() for article in context['object_list']}
        return context


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView): 
    model = Article
    fields = ("title", "body")
    template_name = "article_edit.html"

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView): 
    model = Article
    template_name = "article_delete.html"
    success_url = reverse_lazy("article_list")

    def test_func(self): 
        obj = self.get_object()
        return obj.author == self.request.user


class ProtectedArticleListAPIView(ListAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    permission_classes = [IsAuthenticated]