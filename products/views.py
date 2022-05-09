from django.shortcuts import render, get_object_or_404, redirect
from .forms import ProductForm
from .models import Product
import qrcode
from qrcode import *
from django.contrib.auth.decorators import user_passes_test, login_required
from newspaper_project.decorators import is_admin, is_adminwilaya, is_client, is_livreur

@login_required
@user_passes_test(is_client)

def product_create_view(request):
    form = ProductForm(request.POST or None)
    if form.is_valid():
        user = request.user
        email = user.email
        product = form.save(commit=False)
        product.email = email
        product.save()
        form = ProductForm()
    context = {
        'form': form
    }
    return render(request, "products/new_product_create.html", context)


def product_update_view(request, id=id):
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
    context = {
        'form': form
    }
    return render(request, "products/product_create.html", context)

@login_required
@user_passes_test(is_client)

def product_list_view_client(request):
    user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email) # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

@login_required
@user_passes_test(is_adminwilaya)

def product_list_view_adminwilaya(request):
    user = request.user
    wilaya = user.wilaya
    queryset = Product.objects.filter(wilaya = wilaya) # list of objects
    context = {
        "object_list": queryset
    }
    return render(request, "products/product_list.html", context)

@login_required

def product_detail_view(request, id):
    obj = get_object_or_404(Product, id=id)
    context = {
        "object": obj
    }
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(id)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save("static/image/test.png")
    return render(request, "products/product_detail.html", context)


def product_delete_view(request, id):
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return redirect('../../')
    context = {
        "object": obj
    }
    return render(request, "products/product_delete.html", context)


@login_required

def product_filter_hub(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    search_etape = request.POST.get('etape', None)
    """user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email)"""
    queryset = Product.objects.filter(wilaya = search_wilaya) 
    queryset = queryset.filter(enhub = True) 
    queryset = queryset.filter(typeprestation = search_prestation) 
    queryset = queryset.filter(typeenvoi = search_type) 
    print(queryset)
    context = {
        "object_list": queryset
    }
    return render(request, "pret-a-expedier.html", context)

def product_filter_hub(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    search_type = request.POST.get('type', None)
    search_prestation = request.POST.get('type de prestation', None)
    search_etape = request.POST.get('etape', None)
    """user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email)"""
    queryset = Product.objects.filter(wilaya = search_wilaya) 
    queryset = queryset.filter(enhub = True) 
    queryset = queryset.filter(typeprestation = search_prestation) 
    queryset = queryset.filter(typeenvoi = search_type) 
    print(queryset)
    context = {
        "object_list": queryset
    }
    return render(request, "pret-a-expedier.html", context)

def product_filter_hub(request):
    search_wilaya = request.POST.get('user_wilaya', None)
    print(search_wilaya)
    search_type = request.POST.get('type', None)
    print(search_type)
    search_prestation = request.POST.get('type de prestation', None)
    print(search_prestation)
    search_etape = request.POST.get('etape', None)
    """user = request.user
    email = user.email
    queryset = Product.objects.filter(email = email)"""
    queryset = Product.objects.filter(wilaya = search_wilaya) 
    queryset = queryset.filter(enhub = True) 
    queryset = queryset.filter(typeprestation = search_prestation) 
    queryset = queryset.filter(typeenvoi = search_type) 
    print(queryset)
    context = {
        "object_list": queryset
    }
    return render(request, "En_hub.html", context)
