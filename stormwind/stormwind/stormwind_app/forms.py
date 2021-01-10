from django import forms
from .models import *

class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = '__all__'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'
