from django.shortcuts import render

# Create your views here.
def home(request):

    return render(request, 'order_food_app/index.html')