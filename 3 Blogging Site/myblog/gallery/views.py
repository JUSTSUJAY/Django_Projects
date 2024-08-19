from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Product
from django.contrib import messages
from .forms import ProductForm

# A view that will show all the blogs at the display
def product_list(request):
    product_list = Product.objects.all()   
    return render(request, 'product_list.html', {'product_list': product_list})
    
# suppose a reader wants to read a blog, he will click on it, so we need to take him to the blog page, so we willl need a primary key to retrieve that particular blog

def product_details(request, id):
    # we need to retrieve the blog with the primary key id
    product_requested = Product.objects.get(id = id)
    return render(request, 'product_details.html', {'product_requested':product_requested})

# if an auther wants to edit that product details or anything he should be taken to a new page, there are two cases in this page, either he wants to go to edit and the one where he has done the changes and wants to save it, in which case we will have to redirect it to the listed page

def product_edit(request, id):
    retrieved_product = get_object_or_404(Product, id = id)
    if request.method == 'POST':
        # means the changes have been made and needs to be updated in the database, get that form
        form = ProductForm(request.POST, instance = retrieved_product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = ProductForm(instance = retrieved_product)
    return render(request, 'product_edit.html', {'form':form})

def delete_product(request, id):
    product_to_delete = get_object_or_404(Product, id = id)
    if request.method == "POST":
        product_to_delete.delete()
        return redirect('product_list')
    return render(request, 'product_delete.html', {'product_to_delete':product_to_delete})



