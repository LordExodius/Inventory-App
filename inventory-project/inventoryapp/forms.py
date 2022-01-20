from socket import fromshare
from django import forms
from .models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = "__all__"

class DelForm(forms.Form):
    id = forms.CharField(max_length=100)