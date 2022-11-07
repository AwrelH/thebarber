from . import views
from django.urls import path

urlpatterns = [
    path('', views.BlogPostList.as_view(), name='home'),
    path('<slug:slug>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('upvote/<slug:slug>', views.BlogUpvote.as_view(), name='blog_upvote'),
    
]