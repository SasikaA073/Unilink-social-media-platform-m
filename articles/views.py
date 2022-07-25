from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Article


class ArticleListView(ListView):
    model = Article
    template_name = 'article_list.html'

class ArticleDetailView(ListView):
    model = Article
    template_name = 'article_detail.html'
    fields = ('title', 'body', 'image')


class ArticleCreateView(CreateView):
    model = Article
    template_name = 'article_new.html'
    fields = '__all__'


class ArticleUpdateView(UpdateView):
    model = Article
    template_name = 'article_edit.html'
    fields = ('title', 'body', 'image',)
    

class ArticleDeleteView(DeleteView):
    model = Article
    template_name = 'article_delete.html'
    success_url = reverse_lazy('article_list')