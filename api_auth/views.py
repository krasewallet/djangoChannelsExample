from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.
@api_view(["GET"])
def photos(request):
    data = {
        "code": 0,
        "data": ['http://d.hiphotos.baidu.com/image/pic/item/91ef76c6a7efce1b5ef04082a251f3deb58f659b.jpg'],          
    }
    return Response(data)
