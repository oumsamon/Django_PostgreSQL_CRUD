from django.shortcuts import render, redirect

from .models import Comment, Post
from .forms import PostForm, CommentForm

# Create your views here.
def post_list(request):
    posts = Post.objects.all()
    return render(request, 'scribble/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = Post.objects.get(id=pk)
    return render(request, 'scribble/post_detail.html', {'post': post})

def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
        else:
            form = PostForm()
    else:
        form = PostForm()
    return render(request, 'scribble/post_form.html', {'form': form})

def post_edit(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form=PostForm(instance=post)
    return render(request, 'scribble/post_form.html', {'form': form})

def post_delete(request, pk):
    Post.objects.get(id=pk).delete()
    return redirect('post_list')



def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'scribble/comment_list.html', {'comments': comments})

def comment_detail(request, pk):
    comment = Comment.objects.get(id=pk)
    return render(request, 'scribble/comment_detail.html', {'comment': comment})

def comment_create(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            return redirect('comment_detail', pk=comment.pk)
        else:
            form = CommentForm()
    else:
        form = CommentForm()
    return render(request, 'scribble/comment_form.html', {'form': form})

def comment_edit(request, pk):
    comment = Post.objects.get(id=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save()
            return redirect('post_detail', pk=comment.pk)
    else:
        form=CommentForm(instance=comment)
    return render(request, 'scribble/comment_form.html', {'form': form})

def comment_delete(request, pk):
    Comment.objects.get(id=pk).delete()
    return redirect('comment_list')