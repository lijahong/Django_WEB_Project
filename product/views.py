from django.shortcuts import render
from product.models import Fruits


def createFruitGet(request):
    return render(request, "product/create.html")

def createFruitPost(request):
    fruit = Fruits()
    #model에 data 넣기
    fruit.name = request.POST.get('fname',None)
    fruit.descript = request.POST.get('fdescript', None)
    fruit.price = request.POST.get('fprice', None)
    fruit.quantity = request.POST.get('fquantity', None)
    #db에 저장
    fruit.save()
    return render(request, "product/createResult.html")
"""
def readFruitGet(request):
    fruits = Fruits.objects.all()
    context = {
        'fruits': fruits
    }
    return render(request, "product/read.html", context )
"""
def readFruitGet(request):
    fruits = Fruits.objects.filter(id=1)
    context = {
        'fruits': fruits
    }
    return render(request, "product/createResult.html", context )


