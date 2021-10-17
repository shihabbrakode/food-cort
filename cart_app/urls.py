from django.urls import path
from . import views


urlpatterns=[
    # path('c_det',views.cat_d,name='cat_d'),
    path('cartDetails',views.cart_details,name='cartDetails'),
    path('add/<int:product_id>/',views.add_cart,name='addcart',),
    path('cart-decrement/<int:product_id>/',views.min_cart,name='cart_decrement'),
    path('remove/<int:product_id>/', views.cart_delete, name='remove'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('purchers', views.purchers, name='purchers'),

]