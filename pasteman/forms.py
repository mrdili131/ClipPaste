from django import forms
from .models import Data

class DataCreationForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField()
    is_expired = forms.CheckboxInput()