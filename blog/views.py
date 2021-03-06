from django.shortcuts import render, get_object_or_404
from .models import Blog

# Create your views here.

def allblogs(request):
    blog = Blog.objects.filter().order_by('-id')
    return render(request, 'blog/allblogs.html', {'blogs':blog})

def detail(request, blog_id):
    detail_blog = get_object_or_404(Blog, pk=blog_id)
    return render(request, 'blog/detail.html', {'detail_blog': detail_blog})