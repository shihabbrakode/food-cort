from django.urls import path
from . import views

print('cart5..urls...ok...')
urlpatterns=[
    # path('',views.test,name='test'),
    path('',views.home,name='hm'),
    path('<slug:c_slug>/',views.home,name='prod_cat'),
    path('<slug:c_slug>/<slug:product_slug>',views.proDetails,name='details'),
    path('search',views.serching,name='search')

]