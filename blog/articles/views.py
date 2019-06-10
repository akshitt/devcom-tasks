from django.shortcuts import render ,redirect
from .models import Article
from django.http import HttpResponse 
from django.contrib.auth.decorators import login_required
from . import forms
# Create your views here.
def article_list(request):
    articles = Article.objects.all().order_by('date')

    return render(request,'articles/article_list.html',{'articles' : articles})

def article_details(request,slug):

    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_details.html', {'article':article})

@login_required(login_url="/accounts/login/")
def article_create(request):
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user #would be useful later on for the project
            instance.save()
            return redirect('articles:list')

    else:

        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html',{'form':form})

@login_required(login_url="/accounts/login/")
def edit_post(request,slug):
    post = Article.objects.get(slug=slug)
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST,instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle(instance=post)
    return render(request, 'articles/article_create.html',{'form':form})   






