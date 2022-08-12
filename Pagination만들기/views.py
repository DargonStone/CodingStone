from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator


def index(request):
    Post_list = Post.objects.all()  # queryset containing all movies we just created
    paginator = Paginator(Post_list, 5)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request=request, template_name="blog/index.html", context={'Post_list': page_obj})


# Create your views here.
def post_detail(request, post_id):
    post = Post.objects.get(pk=post_id)

    return render(
        request,
        'blog/post_detail.html',
        {
            'post': post
        }
    )
