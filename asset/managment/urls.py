from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static
from .views import Add_cart    #cart_detail,
from django.contrib.auth import views as auth_views
# from .views import Add_cart
from .views import login



urlpatterns = [
    
    path ('',views.index,name="index"),
    path ("index",views.index,name="index"),

    path('login/', views.login, name="login"),  # Ensure this is correct
    path('loginform', views.loginform, name='loginform'),

    path('staffdashboard',views.staffdashboard,name="staff"),
    path('employee_reg',views.employee_reg,name="employee_reg"),
    path('new_employee',views.new_employee,name="new_employee"),

    path('existing_employee',views.existing_employee,name="existing_employee"),
    path('edit_emp_profile',views.edit_emp_profile,name="edit_emp_profile"),
    path('edit_employee',views.edit_employee,name="edit_employee"),
    path('delete/<int:id>',views.delete,name="delete"),
    path('product_reg',views.product_reg,name="product_reg"),
    path('new_product',views.new_product,name="new_product"),
    path('list_product',views.list_product,name="list_product"),
    path('edit_product',views.edit_product,name="edit_product"),
    path('edit_product_item',views.edit_product_item,name="edit_product_item"),
    path('request_item',views.request_item,name="request_item"),
    path('approved_item',views.approved_item, name='approved_item'),
    # path('non_approved_item',views.non_approved_item, name='non_approved_item'),
    path('delete_product/<int:idp>',views.delete_product,name="delete_product"),
    path('penalty', views.penalty_view, name='penalty_view'),
    path('reject_list/',views.reject_list, name='reject_list'),
    path('user_reg',views.user_reg,name="user_reg"),
    path('new_user',views.new_user,name="new_user"),
    path('staffdashboard',views.staffdashboard,name="staffdashboard"),
    path('userdashboard',views.userdashboard,name="userdashboard"),
   
    

    path('search',views.search,name="search"),
    path('search_details/<s>',views.search_details,name="search_details"),
    path('staff_privacy/',views.staff_privacy, name='staff_privacy'),

    # path('location_list/', views.location_list, name='location_list'),
    # path('locations/add/', views.add_location, name='add_location'),
    # path('cart_view',views.cart_view,name="cart_view"),
    # path('cart_detail', views.cart_detail, name='cart_detail'),
    # path('order_form', views.order_form, name='order_form'),
    # path('cart/', views.view_cart, name='cart'),
    # path('admin_reg',views.admin_reg,name="admin_reg"),
    # path('admin_page',views.admin_page,name="admin_page"),
    # path('admindashboard',views.admindashboard,name="admindashboard"),
    path('Logout',views.Logout,name="Logout"),
    # path('cart_view',views.cart_view,name="cart_view"),
    path('Add_cart', Add_cart, name='Add_cart'),

    path('cart_details', views.cart_details, name='cart_details'),
    path('order_form', views.order_form, name='order_form'),

    # path('payment', views.payment, name='payment'),

    path('delete_cart/<pk>', views.delete_cart, name='delete_cart'),



    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)