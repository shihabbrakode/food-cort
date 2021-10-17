from .models import *
from .views import *


test=9999
def count(request):
    items_count=0
    if 'admin' in request.path:
        return {}
    else:
        try:
            ct=cartlist.objects.filter(cart_id=c_id(request))
            cti=items.objects.all().filter(cart=ct[:1])
            for c in cti:
                items_count+=c.QTY
        except cartlist.DoesNotExixt:
            items_count=0
        return dict(itc=items_count)



