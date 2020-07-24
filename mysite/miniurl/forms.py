from .models import Miniurl
from django import forms

class MiniurlForm(forms.ModelForm):
    class Meta:
        model = Miniurl
        fields = ('original_url', 'short_url')

