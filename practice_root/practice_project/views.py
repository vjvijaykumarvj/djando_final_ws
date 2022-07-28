from django.shortcuts import HttpResponse,render

def Home(request):
    return render(request,'home.html')