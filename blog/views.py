from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.base import View
from .models import Category, Post

#def home(request):
#    if request.method == 'POST':
#        return HttpResponse('Hi')
#    elif request.method == 'GET':
#       return HttpResponse('Good')

class HomeView(View):
    def get(self, request):
        post_list = Post.objects.all()
        return render(request, 'blog/home.html', {'post': post_list})

class CategoryView(View):
    '''Вывод статей категории'''
    def get(self, request, category_name):
        category = Category.objects.get(slug=category_name)
        return render(request, 'blog/post_list.html', {'category': category})

class PostView(View):
    def get(self, reuest, post_name):
        post_list = Post.objects.get(slug=post_name)
        return render(reuest, 'blog/post_view.html', {'post': post_list})