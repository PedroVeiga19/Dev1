from django import forms
from django.core.validators import MinLengthValidator


class ContactForm(forms.Form):
    subject = forms.CharField(label="assunto",
                              max_length=100,
                              validators=[MinLengthValidator(3)],
                              help_text="Informe o assunto")
    email_sender = forms.EmailField(label="email",
                                    help_text="Informe o email")
    message = forms.CharField(label="mensagem",
                              help_text="Informe o mensagem",
                              widget=forms.Textarea())
    cc_myself = forms.BooleanField(required=False,
                                   label="Deseja receber uma cópia?")

    