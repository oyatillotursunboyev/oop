# from django.forms import ModelForm
# from .models import Contact

# class ContactForm(ModelForm):
#     class Meta:
#         model = Contact
#         fields = ['name', 'text']

from django.forms import ModelForm
from django import forms
from .models import Contact


class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'text']

        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3',
                'placeholder': 'Ismingizni kiriting'
            }),

            'text': forms.Textarea(attrs={
                'class': 'w-full border border-gray-300 rounded-lg p-3 h-40',
                'placeholder': 'Xabaringizni yozing'
            })
        }