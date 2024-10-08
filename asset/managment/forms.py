from django import forms


# from .models import Location

# class LocationForm(forms.ModelForm):
#     class Meta:
#         model = Location
#         fields = ['address', 'city', 'state', 'country', 'postal_code', 'image']


# from .models import Admin

# from django import forms
# from .models import Admin

# class AdminForm(forms.ModelForm):
#     class Meta:
#         model = Admin
#         fields = ['state', 'city']

        
from django import forms
from .models import Cart

class CartForm(forms.ModelForm):
    class Meta:
        model = Cart
        fields = ('quantity',)
