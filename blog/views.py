from django.shortcuts import render, redirect
from .models import Blog
from .forms import PostForm
from django.http import HttpResponseRedirect

def index(request):
    stuff = Blog.objects.all()
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            #post = Blog(docfile = request.FILES['docfile'])
            form.save()
            return HttpResponseRedirect('.')
    else:

        return render(request, 'blog/index.html', {'stuff':stuff, 'form':PostForm})
        
def delete_blog(request, blog_id):
    blog_id = int(blog_id)
    try:
        blog_sel = Blog.objects.get(id = blog_id)
    except Blog.DoesNotExist:
        return redirect('index')
    blog_sel.delete()
    return redirect('index')        

def update_blog(request, blog_id):
    blog_id = int(blog_id)
    try:
        blog_sel = Blog.objects.get(id = blog_id)
    except Blog.DoesNotExist:
        return redirect('index')
    blog_form = PostForm(request.POST or None, instance = blog_sel)
    if blog_form.is_valid():
       blog_form.save()
       return redirect('index')
    return render(request, 'blog/update.html', {'form':blog_form})
