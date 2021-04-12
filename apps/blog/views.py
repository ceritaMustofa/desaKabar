from django.core.paginator import Paginator
from django.shortcuts import render, redirect, get_object_or_404

from .models import Post, Categories, CategoryPostDesa, PostDesa
from .forms import CommentForm
# Create your views here.
def indexBerita(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
    }
    return render(request, 'blog_index.html', context)

def post_detail(request, category_slug, slug):
    post = Post.objects.get(slug=slug)

    if request.method == 'POST':
       form = CommentForm(request.POST)
       
       if form.is_valid():
           comment = form.save(commit=False)
           comment.post = post
           comment.save()
           
           return redirect('post_detail', slug=post.slug)
    else:
        form = CommentForm()

    return render(request, 'post_detail.html', {'post': post, 'form':form})


def category_detail(request, slug):
    category = get_object_or_404(Categories, slug=slug)
    posts = category.posts.all()

    paginator = Paginator(posts, 5)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'category': category,
        'page_obj': page_obj,
    }

    return render(request, 'category_detail.html', context)