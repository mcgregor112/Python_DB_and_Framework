from django.shortcuts import render, redirect
from django.http import JsonResponse
import json
from django.contrib import messages

from .models import Blog

def blogs_view(request):
    blogs = Blog.objects.all()
    return render(request, 'dashboard/crud.html', {'blogs':blogs})

def create_blog(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        new_blog = Blog.objects.create(
            title=data['title'],
            content=data['content']
        )
        new_blog.save()
        return JsonResponse({'blog_id':new_blog.id, 'message': 'Blog created successfully'})
    return redirect('blogs_view')

def edit_blog(request, blog_id):
    blog = Blog.objects.get(id=blog_id)
    if request.method == 'POST':
        data = json.loads(request.body)
        blog.title = data['title']
        blog.content = data['content']
        blog.save()
        return JsonResponse({'message': 'Blog updated successfully'})
    return redirect('blogs_view')


def delete_blog(request, blog_id):
    if request.method == 'POST':
        blog = Blog.objects.get(id=blog_id)
        blog.delete()
        return JsonResponse({'message': 'Blog deleted successfully'})
    messages.success(request, 'blog deleted successfully.')
    return redirect('blogs_view')
