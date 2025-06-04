from django.shortcuts import render,HttpResponse,redirect
from . models import Blogs,Category
# Create your views here.
def post_by_category(request,category_id):
    
    posts=Blogs.objects.filter(status='published',category=category_id)
    try:
     category=Category.objects.get(pk=category_id)
    except:
        return redirect('home')
    context={
        'posts':posts,
        'category':category
    }
    return render(request,'posts_by_category.html',context)