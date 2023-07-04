from django.shortcuts import render, redirect, get_object_or_404
from ShopApp.models import Product
from ShopApp.models import Category
from ShopApp.forms import ProductForm, CategoryForm
def products_view(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, "products.html", context)

def product_detail(request, id):
    product = get_object_or_404(Product, id=id)
    return render(request, 'product.html', {'product': product})


def add_category(request):
    if request.method == "GET":
        form = CategoryForm()
        return render(request, "add_category.html", {"form": form})
    else:
        form = CategoryForm(data=request.POST)
        if form.is_valid():
            Category.objects.create(title=form.cleaned_data.get('title'),
                                    description=form.cleaned_data.get('description'))
            return redirect('categories')
        else:
            print(form.errors)
            return render(request, "add_category.html", {"form": form})

def add_product(request):
    if request.method == "GET":
        form = ProductForm()
        return render(request, "add_product.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            Product.objects.create(title=form.cleaned_data.get('title'),
                                   category=form.cleaned_data.get('category'),
                                   price=form.cleaned_data.get('price'),
                                   remainder=form.cleaned_data.get('remainder'),
                                   image=form.cleaned_data.get('image'))
            return redirect('products')
        else:
            print(form.errors)
            return render(request, "add_product.html", {"form": form})

def categories_view(request):
    categories = Category.objects.all()
    context = {'categories': categories}
    return render(request, "categories.html", context)
def delete_category(request, id):
    category = get_object_or_404(Category, id=id)
    category.delete()
    return redirect("categories")

def delete_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "GET":
        return render(request, "delete_product.html", {"product": product})
    else:
        product.delete()
        return redirect("products_view")

def edit_product(request, id):
    product = get_object_or_404(Product, id=id)
    if request.method == "GET":
        form = ProductForm(initial={
            "title": product.title,
            "category": product.category,
            "price": product.price,
            "image": product.image
        })
        return render(request, "edit_product.html", {"form": form})
    else:
        form = ProductForm(data=request.POST)
        if form.is_valid():
            product.title = request.POST.get('title')
            product.category = request.POST.get("category")
            product.price = request.POST.get("price")
            product.remainder = request.POST.get("remainder")
            product.image = request.POST.get("image")
            product.save()
            return redirect("products_views")
        else:
            return render(request, "edit_product.html", {"form": form})

