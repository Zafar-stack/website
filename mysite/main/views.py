from django.shortcuts import render
from main.models import *
from django.http import JsonResponse
from django.db.models import Sum


# Create your views here.
def indexHandler(request):
    get_lang_code = request.GET.get('lang', None)
    if get_lang_code:
        request.session['lang'] = get_lang_code

    get_lang_code = request.GET.get('lang', 'en')
    languages = Language.objects.all()
    products = Product.objects.filter(lang__code=get_lang_code)
    categoriess = Category.objects.order_by('id')[1:4]
    categories = Category.objects.all()
    is_new = Product.objects.filter(is_new=True).filter(lang__code=get_lang_code)
    is_best_saler = Product.objects.filter(is_best_saler=True).filter(lang__code=get_lang_code)

    cart = {}
    cart_items = []

    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    if request.POST:
        email = request.POST.get('email', '')
        pochta = Podpischiki()
        email1 = Podpischiki.objects.filter(email=email)
        if not email1:
            pochta.email = email
            pochta.save()

    return render(request, 'index.html', {
        'categories': categories,
        'categoriess': categoriess,
        'products': products,
        'is_new': is_new,
        'is_best_saler': is_best_saler,
        'cart': cart,
        'cart_items': cart_items,
        'languages': languages,
    })


def blankHandler(request):

    return render(request, 'blank.html', {})


def checkoutHandler(request):

    return render(request, 'checkout.html', {})


def aboutHandler(request):

    return render(request, 'about.html', {})


def contact_usHandler(request):

    return render(request, 'contact_us.html', {})


def productHandler(request, product_id):
    postproduct = Product.objects.get(id=int(product_id))
    product_images = ProductImage.objects.filter(product__id=product_id)
    comment_items = CommentItem.objects.filter(product__id=product_id)

    comment_len = 0
    comment_summa = 0
    reating_orta = 0
    reating_1 = 0
    reating_2 = 0
    reating_3 = 0
    reating_4 = 0
    reating_5 = 0
    reating_1_progress = 0
    reating_2_progress = 0
    reating_3_progress = 0
    reating_4_progress = 0
    reating_5_progress = 0

    for comment in comment_items:
        comment_len += 1
        comment_summa += comment.rating
        if comment.rating == 1:
            reating_1 += 1
        elif comment.rating == 2:
            reating_2 += 1
        elif comment.rating == 3:
            reating_3 += 1
        elif comment.rating == 4:
            reating_4 += 1
        elif comment.rating == 5:
            reating_5 += 1
    if comment_len > 0:
        reating_orta = int(comment_summa / comment_len * 100.0)/100
        reating_1_progress = int(reating_1 / comment_len * 100)
        reating_2_progress = int(reating_2 / comment_len * 100)
        reating_3_progress = int(reating_3 / comment_len * 100)
        reating_4_progress = int(reating_4 / comment_len * 100)
        reating_5_progress = int(reating_5 / comment_len * 100)

    cart = {}
    cart_items = []

    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    return render(request, 'product.html', {'postproduct': postproduct,
                                            'product_images': product_images,
                                            'comment_items': comment_items,
                                            'reating_orta': reating_orta,
                                            'reating_1': reating_1,
                                            'reating_2': reating_2,
                                            'reating_3': reating_3,
                                            'reating_4': reating_4,
                                            'reating_5': reating_5,
                                            'reating_1_progress': reating_1_progress,
                                            'reating_2_progress': reating_2_progress,
                                            'reating_3_progress': reating_3_progress,
                                            'reating_4_progress': reating_4_progress,
                                            'reating_5_progress': reating_5_progress,
                                            'cart': cart,
                                            'cart_items': cart_items,
                                            })

def storeHandler(request):
    get_lang_code = request.GET.get('lang', None)

    if get_lang_code:
        request.session['lang'] = get_lang_code

    get_lang_code = request.session.get('lang', 'en')

    search_value = request.GET.get('q', '')
    category_id = int(request.GET.get('category_id', 0))
    active_category = None
    categories = Category.objects.all()
    is_best_saler = Product.objects.filter(is_best_saler=True).filter(lang__code=get_lang_code)
    total = Product.objects.filter().count()
    languages = Language.objects.all()

    limit = int(request.GET.get('limit', 6))
    current_page = int(request.GET.get('page', 1))
    stop = current_page * limit
    start = stop - limit

    pages_count = int(total / limit)
    if total % limit > 0:
        pages_count += 1
    pages = range(1, pages_count + 1)

    prev_page = current_page - 1
    next_page = 0
    if total > stop:
        next_page = current_page + 1

    cart = {}
    cart_items = []

    open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
    if open_carts:
        open_cart = open_carts[0]
        cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
        cart = open_cart

    if category_id:
        if search_value:
            products = Product.objects.filter(title__contains=search_value).filter(lang__code=get_lang_code)[start:stop]
            total = Product.objects.filter(title__contains=search_value).filter(lang__code=get_lang_code).count()
        else:
            products = Product.objects.filter(category__id=category_id).filter(title__contains=search_value).filter(lang__code=get_lang_code)[start:stop]
            total = Product.objects.filter(category__id=category_id).filter(title__contains=search_value).filter(lang__code=get_lang_code).count()

        active_category = Category.objects.get(id=category_id)
    else:
        if search_value:
            products = Product.objects.filter(title__contains=search_value).filter(lang__code=get_lang_code)[start:stop]
            total = Product.objects.filter(title__contains=search_value).filter(lang__code=get_lang_code).count()
        else:
            products = Product.objects.filter(lang__code=get_lang_code)[start:stop]
            total = Product.objects.filter().filter(lang__code=get_lang_code).count()

    return render(request, 'store.html', {
        'products': products,
        'categories': categories,
        'category_id': category_id,
        'active_category': active_category,
        'search_value': search_value,
        'total': total,
        'is_best_saler': is_best_saler,
        'cart': cart,
        'cart_items': cart_items,
        'prev_page': prev_page,
        'next_page': next_page,
        'limit': limit,
        'current_page': current_page,
        'pages': pages,
        'languages': languages,
                                          })



def cartHandler(request):
    categories = Category.objects.all()
    if not request.session.session_key:
        request.session.create()

    if request.method == 'POST':
        action = request.POST.get('action', '')
        if action == 'add_to_cart':
            new_cart = None
            product_id = int(request.POST.get('product_id', 0))
            amount = int(request.POST.get('amount', 0))
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if not open_carts:
                new_cart = Cart()
                print(request.session.session_key)
                print(request.session)
                new_cart.session_id = request.session.session_key
                new_cart.save()
            else:
                new_cart = open_carts[0]

            cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(product_id=product_id).filter(status=0)
            if cart_items:
                new_cart_item = cart_items[0]
                new_cart_item.amount += amount
                new_cart_item.save()
            else:
                new_cart_item = CartItem()
                new_cart_item.product = Product.objects.get(id=product_id)
                new_cart_item.cart = Cart.objects.get(id=new_cart.id)
                new_cart_item.amount = amount
                new_cart_item.product_price = new_cart_item.product.new_price
                new_cart_item.save()

        elif action == 'remove_from_cart':
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            product_id = int(request.POST.get('product_id', 0))
            new_cart = None
            if open_carts:
                new_cart = open_carts[0]
            if new_cart:
                cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(product_id=product_id).filter(status=0)
                for ci in cart_items:
                    ci.status = -1
                    ci.save()

        elif action == 'checkout':
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if open_carts:
                new_cart = open_carts[0]
                new_cart.last_name = request.POST.get('last_name', '')
                new_cart.fist_name = request.POST.get('fist_name', '')
                new_cart.email = request.POST.get('email', '')
                new_cart.address = request.POST.get('address', '')
                new_cart.city = request.POST.get('city', '')
                new_cart.country = request.POST.get('country', '')
                new_cart.zip_code = request.POST.get('zip_code', '')
                new_cart.phone = request.POST.get('phone', '')

                new_cart.status = 1
                new_cart.save()

        if action in ['add_to_cart', 'remove_from_cart']:
            open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
            if open_carts:
                new_cart = open_carts[0]
                cart_items = CartItem.objects.filter(cart_id=new_cart.id).filter(status=0)
                all_summ = 0
                items_count = 0
                for ci in cart_items:
                    all_summ += ci.amount * ci.product_price
                    items_count += ci.amount
                new_cart.orig_price = all_summ
                new_cart.price = all_summ
                new_cart.amount = items_count
                new_cart.save()

        return JsonResponse({'success': True, '_success': True})
    else:
        cart = {}
        cart_items = []

        open_carts = Cart.objects.filter(session_id=request.session.session_key).filter(status=0)
        if open_carts:
            open_cart = open_carts[0]
            cart_items = CartItem.objects.filter(cart__id=open_cart.id).filter(status=0)
            cart = open_cart

    return render(request, 'checkout.html', {'categories': categories,
                                             'cart': cart,
                                             'cart_items': cart_items,

                                         })


def orderHandler(request):
    orders = Cart.objects.filter(status=0)

    return render(request, 'orders.html', {'orders': orders})


def order_itemHandler(request, order_id):
    order_items = CartItem.objects.filter(status=0).filter(cart__id=order_id)

    return render(request, 'order_item.html', {'order_items': order_items})


def sendMailHandler(request):
    emails = Podpischiki.objects.all()

    email = 'zafarrozikulov@yandex.ru'
    password = 'qazaq_111'
    dest_email = ['rozikulov02@gmail.com']

    subject = 'New Request'
    email_text = 'Hello my friend'

    message = 'From: {}\nSubject: {}\n\n{}'.format(email, subject, email_text)

    server = smtp.SMTP_SSL('smtp.yandex.com')
    server.set_debuglevel(1)
    server.ehlo(email)
    server.login(email, password)
    server.sendmail(email, dest_email, message)
    server.quit()

    return render(request, 'sendmail.html', {'emails': emails})
