from django.core.paginator import Paginator
from django.shortcuts import render
from .models import Post


def post_list(request):
    posts = Post.objects.all()

    per_page = request.GET.get('per_page', 3)
    paginator = Paginator(posts, per_page)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'per_page': per_page,
    }

    return render(request, 'blog/post_list.html', context)