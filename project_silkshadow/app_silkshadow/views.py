from django.shortcuts import render
from app_silkshadow.models import item
from forms import feedback
# Create your views here.
def home(erquest):
    return render(erquest,'app_silkshadow/home.html')

def products(request):
    item_list=item.objects.all()
    my_dict={'item_list':item_list}
    return render(request,'app_silkshadow/product.html',context=my_dict)


def forms(request):
    a=feedback()
    return render(request,'app_silkshadow/forms.html',{'a':a})

