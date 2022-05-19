from django.shortcuts import render
from .models import BlogContent
from django.http import HttpResponse,request
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    blogs = BlogContent.objects.all()
    paginator = Paginator(blogs, 2) # Show 25 contacts per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj
    }
    return render(request,'blog/index.html', context)


def blogView(request, b_id):
    blog = BlogContent.objects.filter(id = b_id)
    
    return render(request, 'blog/blogView.html', {'blog' : blog[0]})