from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.
def index(request):
    posts = Post.objects.all() # will return the array of objects
    p = Paginator(posts, 1)
    page_number = request.GET.get('page')
    try:
        page_obj = p.get_page(page_number)
    except PageNotAnInteger:
        page_obj = p.page(1)
    except EmptyPage:
        page_obj = p.page(p.num_pages)


    return render(request, "index.html", {"page_obj": page_obj})

def post(request,pk):
    posts = Post.objects.get(id = pk)
    return render(request, "post.html", {"posts": posts})
