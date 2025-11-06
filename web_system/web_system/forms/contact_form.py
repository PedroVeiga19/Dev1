from django.core.validators import MinLengthValidator, EmailValidator
from django import forms


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100,
    label="Assunto da mensagem",
    help_text= "Digite o assunto da mensagem",
    validators=[MinLengthValidator(5)]
    )

    sender = forms.EmailField(label="E-mail",
    help_text= "Digite seu endereço de e-mail principal",
    validators=[EmailValidator()])

    message = forms.CharField(
    label="Mensagem",
    help_text= "Digite sua mensagem",
    widget=forms.Textarea)

    cc_myself = forms.BooleanField(required=False, label="Deseja receber uma cópia?")

    def __init__(self,*args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        for new_field in self.visible_fields():
            new_field.field.widget.attrs.update({"class":"form-control"})
        self.fields.get('cc_myself').widget.attrs.pop("class")