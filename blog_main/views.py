from django.shortcuts import render
from blogs.models import Category,Blogs
def home(request):
    # return HttpResponse("<h1>Welcome to the Blog Home Page</h1>")
    categories = Category.objects.all()
    featured_post = Blogs.objects.filter(is_featured=True) 
    context = {
        'categories': categories,
        'featured_post': featured_post
    }
    return render(request,'index.html',context)