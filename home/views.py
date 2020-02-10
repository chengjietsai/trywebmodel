from django.shortcuts import render
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
import forImport_recognize_faces_image
import cv2

# Create your views here.
def index(request):

    #return HttpResponse("<p>Hello world!</p>")
    return render(request,'index.html')


def transfermypic(request):
    if request.method =='POST':#and request.FILES['photoupload']
        #myfile=request.FILES['photoupload']
        #fs = FileSystemStorage()
        #fs.save(myfile.name,myfile)
        forImport_recognize_faces_image.readPara("static/encoding3.pickle",'static/P_20200201_164242.jpg','cnn')

    return render(request,'index.html')


def delmypic(request):
    return render(request,'index.html')