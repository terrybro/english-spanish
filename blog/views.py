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



