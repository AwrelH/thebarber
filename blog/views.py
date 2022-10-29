from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import BlogPost
from .forms import CommentForm
from django.contrib import messages


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
                'commented': False,
                'upvoted': upvoted,
                'post_comment': CommentForm()

            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = BlogPost.objects.filter(status=1)
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.filter(approved=True).order_by('created_on')
        upvoted = False
        if blog.upvotes.filter(id=self.request.user.id).exists():
            upvoted = True

        post_comment_form = CommentForm(data=request.POST)
 
        if post_comment_form.is_valid():
            post_comment_form.instance.name = request.user.username
            post_comment_form.instance.email = request.user.email
            comment = post_comment_form.save(commit=False)
            comment.post = blog
            comment.save()
            messages.success(
                request, 'Your post is successfully posted, wait for approval')
        else:
            post_comment_form = CommentForm()
          
        return render(
            request,
            'blog_detail.html',
            {
                'blog': blog,
                'comments': comments,
                'commented': True,
                'upvoted': upvoted,
                'post_comment': CommentForm()

            },
        )


class BlogUpvote(View):

    def post(self, request, slug):
        post = get_object_or_404(BlogPost, slug=slug)

        if post.upvotes.filter(id=request.user.id).exists():
            post.upvotes.remove(request.user)
        else:
            post.upvotes.add(request.user)

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))
