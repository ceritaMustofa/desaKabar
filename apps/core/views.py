from django.core.paginator import Paginator
from django.shortcuts import render

from apps.blog.models import Post, Categories, PostDesa, CategoryPostDesa
from apps.profiledesa.models import Aparat

# Create your views here.
def frontpage(request):
    menu_profile= PostDesa.objects.all()
    slide_posts = Post.objects.filter(is_featured=True)
    aparat = Aparat.objects.all()
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'menu_profile':menu_profile,
        'slide_post':slide_posts,
        'aparat':aparat,
        'page_obj': page_obj,
        }



    return render(request, 'frontpage.html', context)

