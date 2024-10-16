from django import forms
from short_url.models import ShortUrl


class ShortUrlForm(forms.ModelForm):
    class Meta:
        model = ShortUrl
        fields = ("longUrl",)
        widgets = {"longUrl": forms.TextInput(attrs={"style": "width:300px"})}
