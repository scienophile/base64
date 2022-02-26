from django import forms


class DataForm(forms.Form):
    input_data = forms.CharField(label='input', max_length='100')
