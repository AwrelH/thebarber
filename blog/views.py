from django.shortcuts import render
from django.views import generic
from .models import BlogPost


class BlogPostList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9
    

