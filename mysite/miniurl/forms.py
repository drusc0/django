from django import forms

from .models import Miniurl


class MiniurlForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MiniurlForm, self).__init__(*args, **kwargs)
        self.fields['short_url'].required = False

    class Meta:
        model = Miniurl
        fields = ('original_url', 'short_url')
