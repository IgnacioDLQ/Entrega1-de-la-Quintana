from django import forms

from profesor.models import Profesor

class PersonForm(forms.ModelForm):
    name = forms.CharField(
        label="Nombre del titular",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "person-name",
                "placeholder": "Nombre del titular",
                "required": "True",
            }
        ),
    )
    last_name = forms.CharField(
        label="Apellido del titular",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "person-last-name",
                "placeholder": "Apellido del titular",
                "required": "True",
            }
        ),
    )
    email = forms.EmailField(
        label="Email:",
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "person-email",
                "placeholder": "Email",
                "required": "True",
            }
        ),
    )
    birth_date = forms.DateInput()(
        label="Fecha de nacimiento:",
        max_length=20,
        required=False,
        widget=forms.NumberInput(
            attrs={
                "class": "person-birth-date",
                "placeholder": "Fecha de nacimiento",
                "required": "True",
            }
        ),
    )

    class Meta:
        model = Person
        fields = ["name", "last_name", "email", "birth_date"]
