from django import forms
from .models import *

class InventoryFrm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ('itmName','itmType','itmQty','itmUnit','itmStatus','supplierID')

