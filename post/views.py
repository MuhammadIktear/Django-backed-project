from django.shortcuts import redirect, render
from . forms import postForm
from .models import Post
# Create your views here.
def add_post(request):
    if request.method=='POST':
        post_form=postForm(request.POST)
        if post_form.is_valid():
            post_form.save()
            return redirect('add_post')
    else:
        post_form=postForm()
    return render(request,'add_post.html',{'form':post_form})

def edit_post(request,id):
    post=Post.objects.get(pk=id)
    post_form=postForm(instance=post)
    if request.method=='POST':
        post_form=postForm(request.POST, instance=post)
        if post_form.is_valid():
            post_form.save()
            return redirect('homepage')

    return render(request,'add_post.html',{'form':post_form})
        
def del_post(request,id):
    post=Post.objects.get(pk=id)
    post.delete()
    return redirect('homepage')
        