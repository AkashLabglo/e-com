"""Ecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from re import search
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from wep_app.views import *
from django.conf.urls import include


'''urlpatterns = [ 
    path('search', SearchResultsView.as_view(), name='search_results'),
]'''

urlpatterns = [
    path('grappelli/', include('grappelli.urls')), # grappelli URLS
    path('admin/', admin.site.urls),
    path('', interface, name = "interface"),
    path('search', search, name = "search"),  
    # Cart related urls:-
    path('cart/<pk>', add_cart, name = "add_cart"), 
    path('Show_cart', Show_cart, name = 'Show_cart'), 
    path('remove/<id>', Cart_remove, name = "Car_remove"),
    #path('Orderedby/<id>', Orderedby, name = "Orderedby"), #----saparate_cart prodct get url-----
    path('Orderedby', Orderedby, name = "Orderedby"),  
    path('addquantity/<id>', addquantity, name = "addquantity"), 
    path('Cancel_order/<id>',Cancel_order, name = "Cancel_order" ),
   # path('cancel_all_order/<id>', cancel_all_order, name = 'cancel_all_order'), 
    path('Orderhistory', Orderhistory, name = 'Orderhistory'),   
    # Login/register/logout/password's_Path
    path("login", login, name = "login"),
    path('Logout', Logout, name = 'Logout'), 
    path('register', Register, name = 'register'), 
    # Wish rlated urls:-
    path('wish/<pk>', add_wish, name = "add_wish"),
    path('Show_wish', Show_wish, name = 'Show_wish'), 
    path('wishremove/<id>', wish_remove, name = "wish_remove"),

    
]
# image url to share
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)


'''
order_status = IntegerField(default = 2, choices = ORDER_STATUS)
order_status = IntegerField(default = 2, choices = CART_STATUS)#1.new_order, 2.old_order, 3.not_order 
 added = IntegerField(default = 2, choices = PRODECT_STATUS) # 1.added_wish, 2.added_cart, 3.not_added
 #>>>>>>>>>>>>>>MODEL STAUS CHOISCES<<<<<<<<<<<<<<<<<<<<
# Order
SUCCESS = 1
PENDING = 2
FAILED = 0
ORDER_STATUS = (
    (SUCCESS, 'success'), 
    (PENDING, 'pending'), 
    (FAILED, 'cancel')
)

# Cart
NEWORDER = 1
OLDORDER = 2
NOTORDER = 0
CART_STATUS = (
    (NEWORDER, 'new_order'), 
    (OLDORDER, 'old_order'), 
    (NOTORDER, 'not_order')
)

# prodect
ADDWISH = 1
ADDCART = 2
NOTADDED = 0
PRODECT_STATUS = (
    (ADDWISH, 'added_wish'), 
    (ADDCART, 'added_cart'), 
    (NOTADDED, 'not_added')
)
'''        