from django.shortcuts import render, get_object_or_404, redirect

from apps.blog.models import CategoryPostDesa, PostDesa

# Create your views here.
def indexProfileDesa(request):
    menu = PostDesa.objects.all()
    side_index = PostDesa.objects.get(id=3)

    context = {
        "menu":menu,
        "side_index":side_index,
    }

    return render(request, 'indexProfileDesa.html', context)

def profileDesa_details(request, title):
    menu = PostDesa.objects.all()
    post = get_object_or_404(PostDesa, title=title)

    context = {
        'menu' : menu,
        'post': post
    }
    return render(request, 'profileDesa_details.html', context)



