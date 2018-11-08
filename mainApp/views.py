from django.shortcuts import render

# Create your views here.
def index(reguest):
	return render(reguest, 'mainApp/homePage.html')
def contact(request):
	return render(request, 'mainApp/basic.html', {'values': ['esli busut voprosu dzvoniti po telephone', '(068) 068-68-68']})