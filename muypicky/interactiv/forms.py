from django import forms
from .models import InteractivLocation

class InteractivCreateForm(forms.Form):

    name        = forms.CharField()
    location    = forms.CharField(required=False)
    categorie   = forms.CharField(required=False)

    def clean_nam(self):
        name= self.cleaned_data.get("name")
        if name =="Hello":
            raise forms.ValidationError("Not a valid name")
        return name

class InteractivLocationCreateForm(forms.ModelForm):
    class Meta:
        model = InteractivLocation
        fields = ['name', 'location', 'categorie',]