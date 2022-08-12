import uuid
from shopcart.models import ShopCart


def cart_session(request):
    try:
        cart = ShopCart.objects.get(session_id = request.session['nonuser'], order_placed=False)
    except:
        request.session['nonuser'] = str(uuid.uuid4())
        cart = ShopCart.objects.create(session_id = request.session['nonuser'], order_placed=False)
    return {
        'cart':cart
        }
        

def cartcount(request):
    readcart = ShopCart.objects.filter(user__username = request.user.username, order_placed=False)

    cartread = 0
    for item in readcart:
        cartread += item.quantity

    return {'cartread': cartread}
