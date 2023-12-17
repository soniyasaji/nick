from django.shortcuts import render,redirect
from cart.models import Cart
from newspaper.models import News_Type
from cart.models import Account,Order
from django.contrib.auth.decorators import login_required

app_name="cart"
@login_required
def add_to_cart(request,t):
    type=News_Type.objects.get(ntypname=t)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,type=type)
        if(cart.quantity<cart.type.stock):
            cart.quantity+=1
        cart.save()
    except:
        cart=Cart.objects.create(type=type,user=user,quantity=1)
        cart.save()
    return redirect('cart:cart_view')
@login_required
def cart_view(request):
    total = 0
    user=request.user
    try:
        cart = Cart.objects.filter(user=user)
        for i in cart:
            total+=i.quantity*i.type.price
    except:
        pass

    return render(request,'cartview.html',{'cart':cart,'total':total})


@login_required
def cart_remove(request,t):
    type=News_Type.objects.get(ntypname=t)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,type=type)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()
        else:
            cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def full_remove(request,t):
    type=News_Type.objects.get(ntypname=t)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,type=type)
        cart.delete()
    except:
        pass
    return redirect('cart:cart_view')
@login_required
def order_form(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        user=request.user
        cart=Cart.objects.filter(user=user)
        total=0
        for i in cart:
            total+=i.quantity*i.type.price

        acct=Account.objects.get(acctnumber=n)
        if(acct.balance>total):
            acct.balance=acct.balance-total
            acct.save()
            for i in cart:
                o=Order.objects.create(user=user,type=i.type,phone=p,address=a,noofitems=i.quantity,order_status="paid")
                o.save()
                i.type.stock=i.type.stock-i.quantity
                i.type.save()
            cart.delete()
            msg="Order Placed Successfully"

            return render(request,'orderconfirm.html',{'msg':msg})
        else:
            msg="Insufficient Amount.You can't Placed Order"
            return render(request,'orderconfirm.html',{'msg':msg})

    return render(request,'orderform.html')
@login_required
def order_confirm(request):
    return render(request,'orderconfirm.html')

@login_required
def orderview(request):
    user=request.user
    o=Order.objects.filter(user=user)

    return render(request,'orderview.html',{'o':o,'u':user})






