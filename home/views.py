from django.http.response import HttpResponse
from django.shortcuts import render

# Create your views here.
def index (request):
     return render(request, 'index.html')
def profile(request):
    return render(request, 'profile.html')
def content_management(request):
    return render(request, 'content_management.html')
def demand(request):
    return render(request, 'demand.html')
def sub(request):
    return render(request, 'sub.html')
def service(request):
    return render(request, 'service.html')
def provider(request):
    return render(request, 'provider.html')
def add(request):
    return render(request, 'add.html')
def Service_View(request):
    return render(request, 'view.html')
def notification(request):
    return render(request, 'notification.html')
def driver(request):
    return render(request, 'driver.html')
def add_driver(request):
    return render(request, 'add_driver.html')
def location_view(request):
    return render(request, 'location_view.html')
def map_view(request):
    return render(request, 'map_view.html')
def agent_view(request):
    return render(request, 'agent_view.html')
def charges_view(request):
    return render(request, 'charges_view.html')


  #  return HttpResponse("hiiiii")
