from django import forms
from .models import FeedbackFormModel


class NumberPhone(forms.ModelForm):

    number_phone = forms.CharField(widget=forms.TextInput(attrs={
                "type": "tel",
                "class": 'form__input education__form-input course__form-input form-application__input',
        "placeholder": "+375 __ ___ __ __"
            }))
    name = forms.CharField(required=False, widget=forms.TextInput(attrs={
                "type": "text",
                "class": 'form-application__input',
                "placeholder": 'Введите ваше имя'
            }))
    courser = forms.CharField(required=False, widget=forms.TextInput(attrs={
                'type': 'text',
                'style': 'display:none',
                'class': 'choice__courses form-application__input',
            }))

    class Meta:
        model = FeedbackFormModel
        fields = ['number_phone', 'name', 'courser',]