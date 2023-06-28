from django.shortcuts import render, reverse, redirect, get_object_or_404
from ShopApp.models import Product
from ShopApp.models import Category
from django.http import HttpResponseRedirect, Http404, HttpResponseNotFound

def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products.html", context)

def product_view(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product': product})


def category_add_view(request):
    if request.method == "GET":
        return render(request, "create_category.html")
    if request.method == 'POST':
        Category.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
        )
        return HttpResponseRedirect("/")

def product_add_view (request):
    if request.method == "GET":
        categories = Category.objects.all()
        context = {'categories': categories}
        return render(request, "create_product.html", context)
    elif request.method == 'POST':
        category = get_object_or_404(Category, id=request.POST.get('category'))
        Product.objects.create(
            title=request.POST.get('title'),
            description=request.POST.get('description'),
            category=category,
            created_at=request.POST.get('created_at'),
            price=request.POST.get('price'),
            image=request.POST.get('image')
        )
        return HttpResponseRedirect("/")

def categories_view(request):
    categories = get_object_or_404(Product, id=id)
    context = {'categories': categories}
    return render(request, "categories.html", context)
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return HttpResponseRedirect("/")

def category_edit_view(request, id):
    category = get_object_or_404(Category, id=id)
    if request.method == 'POST':
        category.title = request.POST['title']
        category.description = request.POST['description']
        category.save()
        return redirect('categories_view')
    return render(request, 'category_edit.html', {'category': category})


def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    product.delete()
    return HttpResponseRedirect("/")

def product_edit_view(request, id):
    product = get_object_or_404(Product, id=id)
    categories = Category.objects.all()
    if request.method == 'POST':
        product.title = request.POST['title']
        product.description = request.POST['description']
        category_id = int(request.POST.get('category'))
        category = get_object_or_404(Category, id=category_id)
        product.category = category
        product.price = request.POST.get('price')
        product.image = request.POST.get('image')
        product.save()
        return redirect('product_view', id=id)
    return render(request, 'product_edit.html', {'product': product, 'categories': categories})
