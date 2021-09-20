from django.shortcuts import render

from .models import Comment, Post

# Create your views here.
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comments': comments})






def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})