from django import forms

from student.models import Student

class BankForm(forms.ModelForm):
    name = forms.CharField(
        label="Entidad bancaria",
        max_length=40,
        required=False,
        widget=forms.TextInput(
            attrs={
                "class": "bank-entity",
                "placeholder": "Entidad bancaria",
                "required": "True",
            }
        ),
    )
    class Meta:
        model = Bank
        fields = ["Bank_entity"]
