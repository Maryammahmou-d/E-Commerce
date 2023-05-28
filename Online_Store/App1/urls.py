from django.urls import path
from . import views
urlpatterns = [
   path('',views.login_fun,name="Login"),
   path('Register',views.register_fun,name="Register"),
   path('Logout',views.logout_fun,name="Logout"),
   path('Home',views.home_fun,name="Home"),
   path('Cart',views.user_cart,name="Cart"),
   path('Payment',views.payment_fun,name="Payment"),
   path('product_fun/<int:id>',views.product_fun,name='Product'),
   path('cart/<int:product_id>/', views.cart_fun, name='Cart'),
]