from django.shortcuts import redirect, render ,get_object_or_404
from django.utils import timezone 
from .models import Post 




def post_list(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'back/post_list.html', {'posts': posts})

def post(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'back/post.html', {'posts': posts})

def postList(request):
    posts = Post.objects.order_by('published_date')
    return render(request, 'front/postList.html' , {'posts': posts}) 
    
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'back/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        if request.POST['title'] and request.POST['text']:
            post=Post()
            post.title=request.POST['title']
            post.text=request.POST['text']
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        post = Post()
    return render(request, 'back/post_edit.html', {'post': post})

def post_edit(request, pk):
    npost = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post = npost
        if request.POST['title'] and request.POST['text']:
            post.title=request.POST['title']
            post.text=request.POST['text']
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        post = npost
    
    return render(request, 'back/post_edit.html', {'post': post})