from django.http import HttpResponse
from django.shortcuts import render
from crud.models import myinfo

def read(request):
    datafrommodel=myinfo.objects.all()
    for i in datafrommodel:
        print("first name ",i.fname)
        print("last name ",i.lname)
        print("id no ",i.id_no)
        print("ideas ",i.ideas)
   
    return render (request,'index.html')
def update(request):
    
    return render (request,'index.html')




    # for i in datafrommodel:
    #     print(i.fname)
    #     print(i.lname)
    #     print(i.id_no)
    #     print(i.ideas)
    # print(datafrommodel)
    # params={'name':'arslan'}
     
    # return HttpResponse("Hello this is first page")

def web(request):
    return HttpResponse("Hello this is web page")


def about(request):
    return HttpResponse("Hello this is about page")

def contact(request):
    return HttpResponse("Hello this is contact page")




