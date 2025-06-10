from django.shortcuts import render

# Create your views here.
def  January(request):
    return render(request, 'book/index.html')

def February(request):
    return render(request, 'book/bookdetail.html')