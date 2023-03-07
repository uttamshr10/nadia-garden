from django.shortcuts import render

# Create your views here.
def home(request):
    render(request, 'pizza/home.html')

def order(request):
    render(request, 'pizza/order.html')
