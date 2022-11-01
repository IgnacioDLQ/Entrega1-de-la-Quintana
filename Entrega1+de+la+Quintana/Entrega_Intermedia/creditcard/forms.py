from ckeditor.widgets import CKEditorWidget
from django import forms

from creditcard.models import CreditCard


class CreditCardForm(forms.ModelForm):
    name = forms.CharField(
        label="Titular de la Tarjeta",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "creditcard-name",
                "placeholder": "Nombre del titular",
                "required": "True",
            }
        ),
    )

    code = forms.IntegerField(
        label="Código:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "creditcard-code",
                "placeholder": "Credit Card Code",
                "required": "True",
            }
        ),
    )
    expire_date = forms.IntegerField(
        label="Fecha de Expiracion:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "creditcard-exp-date",
                "placeholder": "Credit Card Expiration Date",
                "required": "True",
            }
        ),
    )


    class Meta:
        model = Course
        fields = ["name", "code", "expire-date"]
