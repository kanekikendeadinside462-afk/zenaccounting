from django import forms

from .models import ContactRequest


class ContactRequestForm(forms.ModelForm):
    class Meta:
        model = ContactRequest
        fields = ["name", "phone", "message"]

    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-3 border-2 border-surface-container-high rounded-xl focus:ring-2 focus:ring-tertiary focus:border-tertiary outline-none transition-all",
                "placeholder": "Иван Иванов",
                "id": "formName",
            }
        )
    )

    phone = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "w-full px-4 py-3 border-2 border-surface-container-high rounded-xl focus:ring-2 focus:ring-tertiary focus:border-tertiary outline-none transition-all",
                "placeholder": "+7 (999) 000-00-00",
                "id": "formPhone",
                "type": "tel",
            }
        )
    )

    message = forms.CharField(
        required=False,
        widget=forms.Textarea(
            attrs={
                "class": "w-full px-4 py-3 border-2 border-surface-container-high rounded-xl focus:ring-2 focus:ring-tertiary focus:border-tertiary outline-none transition-all",
                "placeholder": "Расскажите о вашей компании...",
                "rows": 4,
            }
        ),
    )
