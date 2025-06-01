from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.contrib.auth.decorators import login_required

def post_list(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog_app/post_list.html', {'posts' : posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog_app/post_detail.html', {'post':post})

@login_required
def post_new(request):
    if request.method == "POST":
        title = request.POST['title']
        body = request.POST['body']
        post = Post.objects.create(title = title, body = body, author = request.user)
        
        return redirect('post_detail', pk= post.pk)
    return render(request, 'blog_app/post_form.html')

@login_required
def post_edit(request, post_id):
    post = get_object_or_404(Post, pk = post_id)
    if request.method == "POST":
        post.title = request.POST['title']
        post.body = request.POST['body']
        post.save()
        return redirect('post_detail', pk=post.pk)
    return render(request, 'blog_app/post_form.html', {'post' : post})

@login_required
def post_delete(request, post_id):
    post = get_object_or_404(post, pk = post_id)
    post.delete()
    return redirect('post_list')


