from django.db.models import Count
from django.shortcuts import render, get_object_or_404
from .models import Publications
from .forms import *
# Create your views here.

def publications_page(request):
    query = Publications.objects.all()
    post_form = CategorySearchForm(request.GET or None)
    if post_form.is_valid():
        category = post_form.cleaned_data['category']
        query = query.filter(category__name__icontains=category)
        
    post = query.order_by('category')
    return render(request, 'publications/main.html', locals())

def details(request, slug):
    post = get_object_or_404(Publications, slug=slug)
    return render(request, 'publications/details.html', locals())