from django import forms

from app2.models import *

class product_from(forms.ModelForm):
    class Meta:
        model=Time
        fields='__all__'

class product1_from(forms.ModelForm):
    class Meta:
        model=Maid_deatails
        fields='__all__'
        widgets={'time':forms.RadioSelect}
    
class product2_from(forms.ModelForm):
    class Meta:
        model=Booking
        fields='__all__'