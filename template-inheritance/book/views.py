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

# def February(request):
#     return render(request, 'book/bookdetail.html')
def book_details(request, id):
    try:
        book = Book.objects.get(pk=id)  #1 title rating author
        return render(request, 'book/bookdetail.html', {
            'title':book.title,
            'rating':book.rating
        })
        
    except:
        raise Http404()