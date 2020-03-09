from django import forms


class CalcForm(forms.Form):
    expression = forms.CharField(label='Expression to evaluate', max_length=40)
