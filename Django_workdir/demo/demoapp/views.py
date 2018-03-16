from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Car, Student, Brand, Color
from .forms import CarSearchForm, CreateCarForm
# Create your views here.

def demo_page(request):
	title = 'Demo page'
	page_name = 'Hello World'
	students = Student.objects.all()
	return render(request, "demoapp/index.html", {
		'title': title,
		'page_name': page_name,
		'students': students,
		})

def second_page(request):
	cars = Car.objects.all()
	return render(request, "demoapp/page2.html", locals())
	
def car_details_view(request, id):
	cars = Car.objects.get(id=id)
	return render(request, 'demoapp/car_details.html', locals())

def form_view(request):
	cars_form = CarSearchForm(request.GET or None)
	if cars_form.is_valid():
		brand = cars_form.cleaned_data['brand']
		query = Car.objects.filter(brand__name__icontains=brand)
	else:
		query = Car.objects.all()	
	cars = query.order_by('brand')
	return render(request, 'demoapp/demo-form.html', locals())

def create_car_view(request):
	create_car_form = CreateCarForm(request.POST or None)
	if request.method == 'POST' and create_car_form.is_valid():
		create_car_form.save()
		return redirect(reverse('demo-forms'))
	return render(request, 'demoapp/demo-form-create.html', locals())