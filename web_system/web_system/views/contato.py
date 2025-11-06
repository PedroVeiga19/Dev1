from django.shortcuts import render
from django.views import View
from ..forms.contact_form import ContactForm


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data.get("subject")
            message = form.cleaned_data.get("message")
            sender = form.cleaned_data.get("sender")
            cc_myself = form.cleaned_data.get("cc_myself")

            recipients = ["2024010472@aluno.restinga.ifrs.edu.br"]
            if cc_myself:
                recipients.append(sender)

            context = {
                'recipientes': recipients,
                'form': form,
            }
            return render(request, 'contact/thanks.html', context)

        context = {'form': form,
                   'url_form': 'funcao_contato',
                   }

        return render(request, 'contact/page_contact.html', context)
    elif request.method == 'GET':
        form = ContactForm()
        context = {
            'form': form,
            'url_form': 'funcao_contato'
        }
        return render(request, 'contact/page_contact.html', context)