from msilib.schema import ComboBox
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .models import Product,Contact,Order,OrderUpdate
from math import ceil 
import json

def index(request):
    
    allProds = []
    catprods = Product.objects.values('category', 'id')
    # print("***********************************************************************")
    
    cats = {item['category'] for item in catprods}
    # print(cats)
    
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    # params = {'no_of_slides':nSlides, 'range': range(1,nSlides),'product': products}
    # allProds = [[products, range(1, nSlides), nSlides],
    #             [products, range(1, nSlides), nSlides]]
    params = {'allProds':allProds}
    return render(request, 'shopping/index.html', params)


def about(request):
    return render(request, 'shopping/about.html')
    


def contact(request):
    if request.method == "POST":
        new_name = request.POST.get('name','')
        new_email = request.POST.get('email','')
        new_phone = request.POST.get('phone','')
        new_desc = request.POST.get('desc','')
        new_contact = Contact(name=new_name, email=new_email,phoneno=new_phone,desc=new_desc)
        new_contact.save()
    return render(request, 'shopping/contact.html')


def tracker(request):
    if request.method == "POST":
        orderId = request.POST.get('orderId','')
        email = request.POST.get('email','')
        
        try:
            order = Order.objects.filter(order_id = orderId, email = email)
            if len(order) > 0:
                orderupdates = OrderUpdate.objects.filter(order_id = orderId)
                updates = []
                for item in orderupdates:
                    updates.append({'text' : item.update_desc, 'time' : item.timestap})
                    response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)
            else:
                return HttpResponse("{}")
        except Exception as e:
             return HttpResponse("{}")
        
    return render(request, 'shopping/tracker.html')
   


def product_view(request, my_id):
    product = Product.objects.filter(id = my_id)
    print(product)
    params = {
        'product' : product[0]
    } 
    return render(request, 'shopping/product_view.html', params)


def search(request):
    return render(request, 'shopping/search.html')

def checkout(request):
    thank = False
    id = 0
    if request.method == "POST":
        new_json_data = request.POST.get('itemJson','')
        new_name = request.POST.get('name','')
        new_email = request.POST.get('email','')
        new_phone = request.POST.get('phone','')
        new_address = request.POST.get('address1','') +  " " + request.POST.get('address2','')
        new_city = request.POST.get('city','')
        new_state = request.POST.get('state','')
        new_zip = request.POST.get('zip_code','')
        new_order = Order(items_json = new_json_data ,name=new_name, email=new_email,phoneno=new_phone,
                        address=new_address, city=new_city, state=new_state, zip_code=new_zip)
        new_order.save()
        update = OrderUpdate(order_id = new_order.order_id, update_desc="Your order has been placed")
        update.save()
        thank = True
        id = new_order.order_id
    return render(request, 'shopping/checkout.html', {'thank' : thank, 'id' : id})