from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse
#from django.conf.urls import patterns, url
from django.views.decorators.csrf import csrf_exempt
from django.core.files.storage import FileSystemStorage
from model import emopredict
import pandas as pd


@csrf_exempt
@api_view(['GET'])
def api_root(request):
    x = request.GET.get("x")
    x = int(x)+10
    return Response({
        "Vlaue": x


    })


@csrf_exempt
@api_view(['POST'])
def api_root2(request):
    y = request.GET.get("y")
    y = int(y)+10
    return Response({
        "Vlaue": y


    })


@csrf_exempt
@api_view(['POST'])
def simple_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        signal = pd.read_csv(filename)
        emoresponse = emopredict(signal)
        return Response({
        "Vlaue":emoresponse})
    return Response({
        "Vlaue":"error"})
# Create your views here.

@csrf_exempt
@api_view(['GET'])
def api_root(request):
    x = request.GET.get("x")
    x = int(x)+10
    return Response({
        "Vlaue": x


    })
