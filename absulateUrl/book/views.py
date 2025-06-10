from django.shortcuts import render
from .models import Book
from django.http import Http404
# Create your views here.
def  index(request):
    books = Book.objects.all()
    return render(request, 'book/index.html', 
                  {
                      'books':books
                  })

def February(request):
    return render(request, 'book/bookdetail.html')

def book_details(request, id):
    try:
        book1 = Book.objects.get(pk=id)   #
        print(book1)
        return render(request, 'book/bookdetail.html', {
            'title1':book1.title,
            'author1':book1.author
        })
    except:
        raise Http404()