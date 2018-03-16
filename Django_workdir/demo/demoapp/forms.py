from django import forms
from .models import Car, Brand, Student, Color

class CarSearchForm(forms.Form):
    brand = forms.CharField(min_length=2, max_length=10)
    # model = forms.CharField(required=False)

class CreateCarForm(forms.Form):
    name = forms.CharField()
    year = forms.RegexField(r'^\d{4}')
    brand = forms.ModelChoiceField(queryset=Brand.objects.all())
    color = forms.ModelChoiceField(queryset=Color.objects.all())

    def save(self):
        brand = self.cleaned_data['brand']
        color = self.cleaned_data['color']
        car = Car.objects.create(
    		name=self.cleaned_data['name'],
    		year=self.cleaned_data['year'],	
    		brand = brand,
    	)
        car.color.add(color)