from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import Post

# list of dictionaries of sample data to pass to template


def home(request):
    context = {
        'posts': Post.objects.all()
    }

    return render(request, 'blog/home.html', context)


def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
