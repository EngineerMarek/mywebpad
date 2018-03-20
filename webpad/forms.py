from django import forms

from .models import Webpad

class WebpadForm(forms.ModelForm):

    class Meta:
        model = Webpad
        fields = ('title', 'text',)
