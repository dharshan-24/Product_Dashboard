# from django.shortcuts import render, redirect
# from .models import Product
# from .forms import ProductForm

# def dashboard(request):
#     products = Product.objects.all()
#     return render(request, 'dashboard.html', {'products': products})

# def add_product(request):
#     if request.method == 'POST':
#         form = ProductForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('dashboard')
#     else:
#         form = ProductForm()

#     return render(request, 'add_product.html', {'form': form})


# def cart(request):
#     return render(request, 'cart.html')


# def checkout(request):
#     return render(request, 'checkout.html')


# def success(request):
#     return render(request, 'success.html')

# def add_to_cart(request, product_id):
#     cart = request.session.get('cart', [])

#     cart.append(product_id)

#     request.session['cart'] = cart

#     return redirect('cart')

from django.shortcuts import render, redirect
from .models import Product


def dashboard(request):
    products = Product.objects.all()
    return render(request, 'dashboard.html', {'products': products})


def add_product(request):
    if request.method == "POST":
        title = request.POST.get('title')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES.get('image')

        Product.objects.create(
            title=title,
            price=price,
            description=description,
            image=image
        )

        return redirect('dashboard')

    return render(request, 'add_product.html')


def add_to_cart(request, product_id):

    cart = request.session.get('cart', [])

    cart.append(product_id)

    request.session['cart'] = cart

    return redirect('cart')


def cart(request):

    cart = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart)

    return render(request, 'cart.html', {'products': products})


def checkout(request):

    cart = request.session.get('cart', [])

    products = Product.objects.filter(id__in=cart)

    return render(request, 'checkout.html', {'products': products})


def success(request):

    request.session['cart'] = []

    return render(request, 'success.html')

