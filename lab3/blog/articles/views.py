from django.shortcuts import render
from .models import Article

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})

def archive_item(request):
    return render(request, 'archive.html', {"posts": Article.objects(1)})
# Create your views here.
