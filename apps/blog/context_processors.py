from .models import Categories, CategoryPostDesa

def menu_categories(request):
    categories = Categories.objects.all()

    return {'menu_categories':categories}

def desa_categories(request):
    categories = CategoryPostDesa.objects.all()

    return {'desa_categories': categories}