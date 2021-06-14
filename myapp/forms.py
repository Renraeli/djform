from django import forms


class TextForm(forms.Form):
    text = forms.CharField(label='Matn', max_length=100)
