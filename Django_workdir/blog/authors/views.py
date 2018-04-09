from django.shortcuts import render

# Create your views here.

def authors_page(request):
    return render(request, 'authors/authors.html', locals())