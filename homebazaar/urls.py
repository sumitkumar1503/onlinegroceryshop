"""homebazaar URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LoginView,LogoutView
from bazaar import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home_view,name=''),


    path('login', LoginView.as_view(template_name='bazaar/login.html'),name='login'),
    
    path('afterlogin', views.afterlogin_view,name='afterlogin'),
    path('admin-dashboard', views.admin_dashboard_view,name='admin-dashboard'),
  
    path('logout', LogoutView.as_view(template_name='bazaar/logout.html'),name='logout'),
   
  
    path('admin-product', views.admin_product_view,name='admin-product'),
    path('admin-add-category', views.admin_add_category_view,name='admin-add-category'),
    path('admin-view-category', views.admin_view_category_view,name='admin-view-category'),
    path('delete-category/<int:pk>', views.delete_category_view,name='delete-category'),
    path('update-category/<int:pk>', views.update_category_view,name='update-category'),
    path('customer-view-product-by-category/<int:pk>', views.customer_view_product_by_category_view,name='customer-view-product-by-category'),


    path('delete-product/<int:pk>', views.delete_product_view,name='delete-product'),
    path('delete-order/<int:pk>', views.delete_order_view,name='delete-order'),
    path('update-product/<int:pk>', views.update_product_view,name='update-product'),

    path('terms-and-condition-of-homebazar', views.terms_view,name='terms-and-condition-of-homebazar'),
    path('privacy-policy-of-homebazar', views.privacy_view,name='privacy-policy-of-homebazar'),
    path('aboutus-homebazar', views.aboutus_view,name='aboutus-homebazar'),

    path('order-product/<int:pk>', views.order_product_view,name='order-product'),
   
    path('admin-order', views.admin_order_view,name='admin-order'),
    
    path('all-product', views.all_product_view,name='all-product'),
    path('admin-add-product', views.admin_add_product_view,name='admin-add-product'),
    path('admin-view-product', views.admin_view_product_view,name='admin-view-product'),
]
