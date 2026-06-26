from django.urls import path
from .views import *
from . import views
urlpatterns = [
    
    path("home/", home, name="home"),
    path("about/", about, name="about"),
    #  path("language/", language, name="language"),
    path("xabarlar/", xabarlar, name="xabarlar"),
    path("katalog/", katalog, name="katalog"),
    path("toshirish_punkiti/", topshirish_punkiti, name="topshirish_punkiti"),
    path("sotuvchi_bolish/", Sotuvchi_bolish, name="sotuvchi_bolish"),  
    path("sotuvchi_bolish_login/", sotuvchi_bolish_login, name="sotuvchi_bolish_login"),
    path("punkitni_ochish/", punkitni_ochish, name="punkitni_ochish"),
    path("savol-javob/", savol_javob, name="savol_javob"),
    path("product_detail/<int:id>/", product_detail, name="product_detail"),
    path("mother_and_children/", Mother_and_Children, name="Mother"),
    path("", split, name="split"),
    path('add-to-cart/<int:item_id>/', add_to_cart, name='add_to_cart'),
    path('cart/', cart_page, name='cart_page'),
    path("navigation/<int:id>/", views.navigation, name="navigation"),
      path(
        'remove-from-cart/<int:item_id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),
]
