from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import BlogPost


class BlogPostList(generic.ListView):
    model = BlogPost
    queryset = BlogPost.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 9
    

class BlogDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        if blog.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True
        
        return render(
            request,
            'blog_detail.html',
            {
                'blog': blog,
                'comments': comments,
                'upvoted': upvoted
                
            },
        )