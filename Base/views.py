from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, get_object_or_404
from .models import CartItem, Contact
from .forms import ContactForm


@login_required 
def about(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid(): # ==== toldirilgan yoki toldirilmagan degani
            form.save()
            return redirect('about')
    else:
        form = ContactForm()    

    messages = Contact.objects.all()

    return render(request, 'about.html', {"form" : form, "messages": messages})
    


def home(request):

    items = Item.objects.all()
    men = Men.objects.all()
    main_picture = Main_branch.objects.all()
    categories = Category.objects.all()


    return render(request, "index.html", {
        "items": items,
        "men": men,
        "main_picture": main_picture,
        "categories": categories,
    })

def navigation(request, id):

    category = get_object_or_404(
        Category,
        id=id
    )

    products = Item.objects.filter(
        category=category
    )


    return render(
        request,
        "index.html",
        {
            "products": products,
            "category": category,
        }
    )




def footer(request):
    return render(request, "footer.html")


def topshirish_punkiti(request):
    return render(request, "topshirish_punkiti.html")

def Sotuvchi_bolish(request):
    return render(request, "sotuvchi_bolish.html")

def sotuvchi_bolish_login(request):
    return render(request, "sotuvchi_bolish_login.html")

def katalog(request):
    return render(request, "katalog.html")

def xabarlar(request):
    messages = Contact.objects.all()
    return render(request, "xabarlar.html", {"messages": messages})

def punkitni_ochish(request):
    return render(request, "punkitni_ochish.html")


def savol_javob(request):
    return render(request, "Base/savol_javob.html")

# def language(request):
#     return render(request, "Base/language.html")

def product_detail(request, id):
    narsalar = get_object_or_404(Item, id=id)
    return render(request, "product_detail.html", {"narsalar": narsalar})

def Mother_and_Children(request):
    return render(request, "mother_and_children.html")

def split(request):
    return render(request, "split.html")



def add_to_cart(request, item_id):
    item = get_object_or_404(Item, id=item_id)
    
    cart, created = Cart.objects.get_or_create(user=request.user)

    cart_item, created = CartItem.objects.get_or_create(cart=cart, item=item)
    
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect("cart_page")


    
def cart_page(request):
    cart = Cart.objects.get(user=request.user)

    items = cart.cartitem_set.all()

    return render(request, 'cart.html', {
        'items': items
    })
def remove_from_cart(request, item_id):
    cart_item = get_object_or_404(CartItem, id=item_id)

    if request.method == "POST":
        cart_item.delete()

    return redirect('cart_page')

    