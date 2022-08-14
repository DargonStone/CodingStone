from django.shortcuts import render
from .models import Post,Category
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def index(request):
    Post_list = Post.objects.all().order_by('-create_time')
    categories = Category.objects.all()
    paginator = Paginator(Post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="blog/index.html", context={'Post_list': page_obj, 'categories': categories})


# Create your views here.
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)
    categories = Category.objects.all()

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post, 'categories' : categories
        }
    )


def search(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query)).distinct()
    paginator = Paginator(posts_list, 5)  # 6 posts per page
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'Post_list': posts
    }
    return render(request, "blog/search.html", context)


def category_page(request, slug):
    category = Category.objects.get(slug=slug)
    categories = Category.objects.all()
    paginator = Paginator(categories, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render (
        request,
        'blog/category_view.html',
        {
            'post_list' : Post.objects.filter(category=category),
            'categories' : categories,
            'Post_list' : page_obj
        }
    )

