from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import posts
from django.views.generic import TemplateView
from .forms import ListForm

# Create your views here.

def index(request):
    return render(request,"first_app/index.html",)

def about(request):
    return render(request,"first_app/about.html",)

def postt(request):
    post_list = posts.objects.all()
    return render(request,"first_app/posts.html",{'post_list' : post_list})





def create(request):
    if request.method ==  "POST":
        form = ListForm(request.POST or None)
        if form.is_valid:
            form.save()
            post_list = posts.objects.all()    
            return render(request,"first_app/create.html",{'post_list':post_list})

    else:
        post_list = posts.objects.all()    
        return render(request,"first_app/create.html",{'post_list':post_list})

def delete(request,posts_id):
    post=posts.objects.get(pk=posts_id)
    post.delete()
    return redirect("posts")   



def update(request,posts_id):
    if request.method ==  "POST":
        post_list=posts.objects.get(pk=posts_id)
        form = ListForm(request.POST or None, instance=post_list)
        if form.is_valid:
            form.save()   
            return redirect("posts")

    else:
        post_list = posts.objects.all()    
        return render(request,"first_app/create.html",{'post_list':post_list})