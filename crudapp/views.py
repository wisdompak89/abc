from django.shortcuts import render

# Create your views here.
def home(requsest):
    return render(requsest, 'home.html')