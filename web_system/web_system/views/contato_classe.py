from django.shortcuts import render
from django.views import View
from .contato import ContactForm

class ContactView(View):
    @staticmethod
    def get(request):
        form = ContactForm
        context = {'form':form,
                   'url_form':'classe_contato'}
        return render(request,'contact/page_contact.html',context)