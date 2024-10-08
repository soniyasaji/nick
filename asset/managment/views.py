from django.shortcuts import get_object_or_404, redirect
from .models import Product, User

from django.shortcuts import render, get_object_or_404, redirect


from django.shortcuts import render

from django.shortcuts import get_object_or_404, redirect

from django.shortcuts import render,redirect,get_object_or_404
from.models import Employee as emp,login as log,Product as pro,Request as re,User as user,CartItem
from .models import Product

from django.contrib import messages


from django.contrib.auth.decorators import login_required

# from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth import authenticate, login
from . views import login # Assuming you have a form defined

from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User,auth

from django.http import HttpResponse

from django.contrib.auth.hashers import check_password, make_password


from django.db.models import Q
from django.core.files.storage import FileSystemStorage

def index(request):
    return render (request,"index.html")

def employee_reg(request):
    return render(request,'employee_reg.html')


def new_employee(request):
    if request.method =='POST':
        c1=request.POST.get("a1")
        print(c1)
        c2=request.POST.get("a2")
        c3=request.POST.get("a3")
        c4=request.POST.get("a4")
        c5=request.POST.get("a5")
        c6=request.POST.get("a6")  
        c7=request.POST.get("a7")
        c8=request.POST.get("a8")
        c9=request.POST.get("a9")
        data=log.objects.create(username=c8,password=c9,role="employee")
        emp.objects.create(Employee_name=c1,Designation=c5,Address=c2,Gender=c4,Phone=c3,Place=c6,Email=c7,logid=data)
        response=redirect("employee_reg")
        return response
    return render(request,'employee_reg.html')

def user_reg(request):
    return render(request,'user_reg.html')

def new_user(request):
    if request.method == 'POST':
        fname = request.POST.get("fname")
        lname = request.POST.get("lname")
        phone = request.POST.get("phone")
        dob = request.POST.get("dob")
        gender = request.POST.get("gender")
        state = request.POST.get("state")
        city = request.POST.get("city")
        address = request.POST.get("address")
        pincode = request.POST.get("pincode")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # Create the login object
        user_data = log.objects.create(username=username, password=password, role="user")
        user_inf = log.objects.last()
        # Create the user object with the foreign key reference to log_user_id
        user.objects.create(
            first_name=fname,
            last_name=lname,
            pincode=pincode,
            address=address,
            gender=gender,
            state=state,
            city=city,
            phone_number=phone,
            date_of_birth=dob,
            email=email,
            log_user_id=user_inf  # Use log_user_id to link the login object
        )
        

        response = redirect("user_reg")
        return response
    return render(request, 'user_reg.html')
def login(request):
    return render (request,"login.html")

def loginform(request):
    if request.POST:
        user = request.POST["username"]
        Password = request.POST["password"]
        try:
            datac = log.objects.filter(username=user, password=Password).count()
            if datac == 1:
                datac = log.objects.get(username=user, password=Password)
                if datac.role == "staff":
                    request.session['username'] = datac.username
                    request.session['role'] = datac.role
                    request.session['id'] = datac.login_id
                    response = redirect('/staffdashboard')
                    return response
                    
                elif datac.role == "admin":
                    request.session['username'] = datac.username
                    request.session['role'] = datac.role
                    request.session['id'] = datac.login_id
                    response = redirect('/admindashboard')
                    return response

                elif datac.role == "Employee":
                    request.session['username'] = datac.username
                    request.session['role'] = datac.role
                    request.session['id'] = datac.login_id
                    response = redirect()
                    return response


                elif datac.role == "user":
                    request.session['username'] = datac.username
                    request.session['role'] = datac.role
                    request.session['id'] = datac.login_id
                    response = redirect('/userdashboard')
                    return response
                    
                    
            else:
                response = redirect('/index?msg=invalid username or password')
                return response   
        except:
            response = redirect('/index?msg=something went wrong')
            return response
    else:
        response = redirect('/index')
        return response


def staffdashboard(request):
    return render(request,'staffdashboard.html')






def existing_employee(request):
    empf = emp.objects.all()
    return render(request,"existing_employee.html",{"empf":empf})

def edit_emp_profile(request):
    ids = request.GET["id"]
    data = emp.objects.filter(Employee_id=ids)
    
    # Print data details
    for employee in data:
        print(f"Employee ID: {employee.Employee_id}")
        print(f"Name: {employee.Employee_name}")
        print(f"Department: {employee.Designation}")
        print(f"Address: {employee.Address}")

        # Add more fields as needed
    
    return render(request, "edit_emp_profile.html", {"data":data})

def edit_employee(request):
    e1=request.POST.get("e1")
    e2=request.POST.get("e2")  
    e3=request.POST.get("e3")
    e5=request.POST.get("e5")
    e6=request.POST.get("e6")
    e7=request.POST.get("e7")
    e8=request.POST.get("e8")
    e9=request.POST.get("e9")
    e10=request.POST.get("e10")
    empid=request.POST.get("empid")
      
    emp.objects.filter(Employee_id=empid).update(Employee_name=e1,Address=e2,Phone=e3,Designation=e5,Place=e6,Email=e7)
    data = emp.objects.filter(Employee_id=empid)
    return render(request,"edit_emp_profile.html",{"msg": "", "data": data})
        


def delete(request, id):
    try:
        mem = emp.objects.get(Employee_id=id)
        mem.delete()
        return redirect('existing_employee')
    except emp.DoesNotExist:
        # Handle the case where the employee does not exist
        return redirect('existing_employee')

def product_reg(request):
    return render(request,"product_reg.html")

def new_product(request):
    if request.method == 'POST':
        p1 = request.POST.get("d1")
        print(p1)
        p2 = request.FILES["d2"]

        fs = FileSystemStorage()
        filename = fs.save(p2.name, p2)
           
        p3 = request.POST.get("d3")
        print(p3)
        p4 = request.POST.get("d4")
        print(p4)
        p5 = request.POST.get("d5")
        print(p5)
        p6=request.POST.get("d6")
        
        pro.objects.create(
            Product_Name=p1,
            Image=filename,
            Description=p3,
            Specification=p4,
            Quantity=p5,
            Amount=p6
        )
        
        response = redirect("product_reg")
        return response
    
    return render(request, "product_reg.html")

def list_product(request):
    listprod = pro.objects.all()
    return render(request,'list_product.html',{"listprod":listprod})

def edit_product(request):
    pid = request.GET["id"]
    pdata = pro.objects.filter(Product_id=pid)
    
    # Print productdata details
    for product in pdata:
        print(f"Product ID: {product.Product_id}")
        print(f"Product Name: {product.Product_Name}")
        print(f"Image: {product.Image}")
        print(f"Description: {product.Description}")
        print(f"Specification: {product.Specification}")
        print(f"Quantity: {product.Quantity}")
        print(f"Amount: {product.Amount}")
         # Add more fields as needed
    
    return render(request, "edit_product.html", {"pdata":pdata})

def edit_product_item(request):
    proname = request.POST.get("proname")
    prodes = request.POST.get("prodes")
    prospec = request.POST.get("prospec")
    proqn = request.POST.get("proqn")
    proamt = request.POST.get("proamt")
    pid = request.POST.get("prodinf")
    
    # Check if a new image has been uploaded
    if 'proimage' in request.FILES:
        proimage = request.FILES['proimage']
        fs = FileSystemStorage()
        filename = fs.save(proimage.name, proimage)
    else:
        # If no new image is uploaded, retain the existing image
        existing_product = pro.objects.get(Product_id=pid)
        filename = existing_product.Image  # Keep the existing image

    # Update the product details
    pro.objects.filter(Product_id=pid).update(
        Product_Name=proname,
        Image=filename,
        Description=prodes,
        Specification=prospec,
        Quantity=proqn,
        Amount=proamt
    )

    pdata = pro.objects.filter(Product_id=pid)
    return render(request, 'edit_product.html', {"pdata": pdata})

def request_item(request):
    requestitem = re.objects.all()
    return render(request,'request_item.html',{"requestitem":requestitem})



def approved_item(request):
    # Filter requests where Status is "approved"
    approved_items = Penalty.objects.all()
    # Render the approved_item.html template with the filtered items
    return render(request, 'penalty_view.html',{"pen":approved_items})
    
def penalty_view(request):
    pen = Penalty.objects.all()  # Fetch all penalties to display in the template
    context = {
        'pen': pen
    }
    return render(request, 'penalty_view.html', context)



def reject_list(request):
    rejected_items = re.objects.all()  # Filter rejected items
    context = {
        'rejected_items': rejected_items
    }
    return render(request, 'reject.html', context)


# def non_approved_item(request):
    # Get all request items where the status is not "approved"
    # non_approved_items = re.objects.exclude(Status="approved")
    
    # Render the approved_item.html template with the filtered request items
    # return render(request, 'non_approved_item.html', {"requestitem": non_approved_items})

def delete_product(request, idp):
    try:
        delprod = re.objects.get(Product_id=idp)
        delprod.delete()
        return redirect('request_item')
    except pro.DoesNotExist:
        # Handle the case where the employee does not exist
        return redirect('request_item')




def search(request):
    query=""
    search_details=None
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            search_details=pro.objects.filter(Q(Product_Name__icontains=query) | Q(Description__icontains=query))
    return render(request,'search.html',{'s':search_details,'q':query})   

def search_details(request,s):
    d=pro.objects.get(Product_Name=s)
    return render(request,'search_details.html',{'d':d})

def staff_privacy(request):
    login_id = request.session['id']
    if request.method == 'POST':
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        pwd= log.objects.get(login_id=login_id)
        
        if current_password==pwd.password :
            print(pwd.password)
            log.objects.filter(login_id=login_id).update(password=new_password)
        
           
    return render(request, 'staff_privacy.html')


def messages(request):
    return render(request,'messages.html')

# from .models import CartItem

# from .models import Location,CartItem

# def add_location(request):
#     if request.method == "POST":
#         form = LocationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('location_list')
#     else:
#         form = LocationForm()
#     return render(request, 'add_location.html', {'form': form})

# def location_list(request):
#     locations = Location.objects.all()
#     return render(request, 'location_list.html', {'locations': locations})




# def add_location(request):
#     if request.method == "POST":
#         form = LocationForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('location_list')
#     else:
#         form = LocationForm()
#     return render(request, 'add_location.html', {'form': form})

# def location_list(request):
#     locations = Location.objects.all()
#     return render(request, 'location_list.html', {'locations': locations})

def userdashboard(request):
    user_products=pro.objects.all()
    cart=CartItem.objects.count()
    
    return render(request,"userdashboard.html",{'user_products':user_products,'cart':cart})
# def admin_reg(request):
#     return render(request,'admin_reg.html')



# def admin_page(request):
#     if request.method == 'POST':
#         adminform = AdminForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('admin_reg')  # Assuming 'admin_reg' is a named URL pattern
#     else:
#         form = AdminForm()

#     return render(request, 'admin_reg.html', {'adminform': adminform})


# def admindashboard(request):
#     return render(request, 'admindashboard.html')

def Logout(request):
    try:
        del request.session['id']
        del request.session['role']
        del request.session['username']
        response = redirect("/index")
        return response
    except:
        response = redirect("/index")
        return response

from .models import Product, CartItem


def Add_cart(request):
    # Retrieve product and user from POST data
    Product_id = request.POST["pid"]
    u_id = request.POST["uid"]

    # Get the product and user objects from the database
    product = get_object_or_404(Product, Product_id=Product_id)
    usr = get_object_or_404(user, log_user_id=u_id)
    
    # Get or create a CartItem instance
    cart_item, created = CartItem.objects.get_or_create(
        user=usr,
        product=product
    )
    
    # If the CartItem already exists, increase the quantity
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        # Save the new CartItem instance
        cart_item.save()
     
    
    
    # Redirect to the user dashboard
    return redirect('userdashboard')


def add_to_cart(request, product_id):
    product = get_object_or_404(pro, Product_id=Product_id)
    cart_item, created = CartItem.objects.get_or_create(
        user=request.user,
        product=product
    )
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    else:
        cart_item.save()

    messages.success(request, f"{product.name} has been added to your cart.")
    return redirect('cart_detail')



def cart_details(request):
    cart_details=CartItem.objects.all()
    return render(request, 'cart_details.html',{'cart_details':cart_details})

def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(CartItem, id=cart_item_id, user=request.user)
    cart_item.delete()
    messages.success(request, "Item has been removed from your cart.")
    return redirect('cart_detail')


# def cart_view(request):
#     user=request.user
#     cart_view=CartItem.objects.filter(user_id=user.id)
#     total=0
    
#     for i in cart_view:
#         total+=i.quantity*i.product.price
#     return render(request,'cart_view.html',{'cart_view':cart_view,'total':total})

# # def cart_remove(request,pk):
# #     instance=CartItem.objects.get(pk=pk)
# #     instance.delete()
# #     cart_detail=CartItem.objects.all()
# #     return render(request,'cart_details.html',{'cart_detail':cart_detail})

def delete_cart(request, pk):
    try:
        delcart = CartItem.objects.get(id=pk)
        delcart.delete()
        return redirect('cart_details')
    except CartItem.DoesNotExist:
        # Handle the case where the employee does not exist
        return redirect('cart_details')


def order_form(request):
    if(request.method=="POST"):
        a=request.POST['a']
        p=request.POST['p']
        n=request.POST['n']
        user=request.user
        cart=CartItem.objects.filter(user=user)
        total=0
        for i in cart:
            total+=i.quantity*i.product.price
        acct=Account.objects.get(acctnumber=n)
        if(acct.balance>=total):
            acct.balance=acct.balance-total
            acct.save()
            for i in cart:
                o=Order.objects.create(user=user,product=i.product,phone=p,address=a,
                                       noofitems=i.quantity,order_status="paid")
                o.save()
                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            cart.delete()
            msg="Order Placed Successfully"

            return render(request,'orderconfirm.html',{'msg':msg})
        else:
            msg="Insufficiant Amount.You can't unable to Place Order"
            return render(request,'orderconfirm.html',{'msg':msg})
    return render(request,'order_form.html')




def orderview(request):
    user=request.user
    o=Order.objects.filter(user=user)

    return render(request,'orderview.html',{'o':o,'u':user.username})

