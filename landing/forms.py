from django import forms
from .models import Application

class ApplicationForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'contact', 'goal']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Алия'}),
            'contact': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '@yourtg или email'}),
            'goal': forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'placeholder': 'Например: TOPIK, с нуля, хочу понимать дорамы'}),
        }

class ContactForm(forms.Form):
    name = forms.CharField(label='Ваше имя')
    email = forms.EmailField(label='Email')
    message = forms.CharField(widget=forms.Textarea, label='Сообщение')
    honeypot = forms.CharField(required=False, widget=forms.HiddenInput)