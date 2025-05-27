from django.shortcuts import render,redirect,HttpResponse
from .models import *
from.forms import*
from django.http import JsonResponse

# Create your views here.
def shop(request):
    chair=Chair.objects.all()
    context={'chair':chair}
    return render(request,'shop.html',context)

def createitem(request):
    chair=ChairModelForm()
    if request.method=="POST":
        chair=ChairModelForm(request.POST,request.FILES)
        if chair.is_valid():
           
            chair.save()
          
            return redirect('/shop')
        else:
           
            return HttpResponse('Error')
    return render(request,'createitem.html',{'chair':chair})


def cartview(request):
    inv_no = request.session.get('invoice_no',None)
    cart_product = Cart.objects.get(id=inv_no)
    context={'cart': cart_product}
    return render(request,'cart.html',context)

def addtocart(request):
    pid=request.GET.get('product_id')
    product_obj=Chair.objects.get(id=pid)
    inv_no=request.session.get('invoice_no',None) # invoice is already exists or not
    if inv_no:  #if invoice exists
        
        cart_obj=Cart.objects.get(id=inv_no)  #use id of innvoice_no that exists
        prod_exist=cart_obj.cartproduct_set.filter(product=product_obj)   #product is already exists or not
        if prod_exist:  #if the product exists
            prod_item=prod_exist.first()
            prod_item.qty+=1
            prod_item.total = prod_item.qty * prod_item.amount
            prod_item.save()  
           
        else:   #product not exsits
            
            cp_obj=CartProduct.objects.create(cart=cart_obj,product=product_obj,qty=1,amount=product_obj.price)

    else:  # invoice not exits
         
        cart_obj=Cart.objects.create(total=0)
        request.session["invoice_no"] = cart_obj.id 
        cp_obj=CartProduct.objects.create(cart=cart_obj,product=product_obj,qty=1,amount=product_obj.price)

        
    return redirect('cartview')

def deletecart(request,id):
    cart_data=CartProduct.objects.filter(id=id).delete()
    return redirect('cartview')

def checkout(request):
    return render(request,'checkout.html')

def addcart(request):
    name=request.GET['name']
    price=request.GET['price']
    CartProduct.objects.create(
        name=name,
        amount=price
    )
    return JsonResponse({'status':'success'})