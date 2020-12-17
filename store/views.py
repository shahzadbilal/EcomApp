from django.shortcuts import render, redirect
from .models import Product, Category, Cart, CartItem

# Create your views here.
# def home(request):
#     products = Product.objects.filter(available=True).order_by('price')
#     links = Category.objects.all()
#     context = {'products': products, 'links': links}
#     return render(request, 'home.html', context)

def home(requset, category_slug=None):
    category_page = None
    if category_slug:
        products = Product.objects.filter(category__slug=category_slug)
    else:
        products = Product.objects.filter(available=True)
    context = {'category': category_page, 'products': products}
    return render(requset, 'home.html', context)

def about(request):
    return render(request, 'about.html')



# def productDetail(request):
#     return render(request, 'product.html',{})

def productDetail(request, category_slug, product_slug):
    try:
        product = Product.objects.get(category__slug=category_slug, slug=product_slug)
    except Exception as e:
        raise e
    return render(request, 'product.html', {'product': product})

def cart(request):
    return render(request, 'cart.html')

def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart

def add_cart(request, product_id):
    product = Product.objects.get(id=product_id)
    cart, created = Cart.objects.get_or_create(cart_id=cart_id(request))

    try: # update if exists
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.stock:
            cart_item += 1
        cart_item.save()
    except CartItem.DoesNotExist: # creating new cart item
        cart_item = CartItem.objects.create(product=product, quantity=1, cart=cart)
        cart_item.save()
    return redirect ('home')


