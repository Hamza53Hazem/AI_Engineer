from django import forms

from .models import ContactMessage


class ContactForm(forms.ModelForm):
    """Simple contact form backed by the ContactMessage model."""

    class Meta:
        model = ContactMessage
        fields = ["name", "email", "message"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Your name"}),
            "email": forms.EmailInput(attrs={"placeholder": "you@example.com"}),
            "message": forms.Textarea(attrs={"rows": 4, "placeholder": "How can we help? (Up to 2000 characters)"}),
        }
