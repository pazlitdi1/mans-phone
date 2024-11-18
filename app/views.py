from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from django.utils.text import slugify
import itertools


def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'index.html', context)


def index_item(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'detail.html', context)


def add_item(request):
    if request.method == "POST":
        title = request.POST.get("title", "")
        slug = generate_unique_slug(Product, title, 'slug')  # Передаем класс модели
        products = Product(
            title=title,
            slug=slug,
            description=request.POST.get("description", ""),
            price=request.POST.get("price", 0),
            image=request.FILES.get("image")
        )
        products.save()
        return render(request, 'success.html', {'product': products})
    return render(request, 'add_item.html')


def generate_unique_slug(model_class, title, slug_field):
    slug = slugify(title)
    unique_slug = slug
    num = 1

    # Проверяем уникальность slug в переданной модели
    while model_class.objects.filter(**{slug_field: unique_slug}).exists():
        unique_slug = f"{slug}-{num}"
        num += 1

    return unique_slug