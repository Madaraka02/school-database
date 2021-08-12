from django import forms
from django.forms import ModelForm


class AddItemImagesForm(ModelForm):
    class Meta:
        model = ItemImages
        fields = '__all__'
        widgets = {
            'image':forms.FileInput(attrs={'multiple':True})