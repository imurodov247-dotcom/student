from django.shortcuts import render

# Create your views here.
def inex(request):
    return render(request, "student/index.html")