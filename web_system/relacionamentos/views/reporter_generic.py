from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView

from relacionamentos.models import Reporter
from relacionamentos.forms import ReporterForm


class ReporterListViewGeneric(ListView):
    model = Reporter # código do professor
    template_name = "reporter/list.html" # código do professor
    context_object_name = 'lista' # código do professor
    # Avoid querying the database at import time; set an empty queryset by default
    queryset = Reporter.objects.none()


    def get_queryset(self):
        objects = Reporter.objects.all()
        #objects = Reporter.objects.find_by_name('Fer')# código do professor
        #other_objects = Perfil.objects.find_by_passaporte('111')# código do professor
        #objects = objects.union(other_objects)# código do professor não consigo fazer o union funcionar perguntar sobre o order_by do html

        return objects


class ReporterDetailsViewGeneric(DetailView):
    model = Reporter # código do professor
    # fields = '__all__' # código do professor
    template_name='reporter/read.html' # código do professor
    # sucess_url = reverse_lazy('relacionamentos:reporter_list_generic') # código do professor
    context_object_name = 'objeto_reporter'


class ReporterDeleteViewGeneric(DeleteView):
    model = Reporter # código do professor
    # fields = '__all__' # código do professor
    template_name = 'reporter/delete.html' # código do professor
    success_url = reverse_lazy('relacionamentos:reporter_list_generic') # código do professor
    context_object_name = 'objeto_reporter'


class ReporterCreateViewGeneric(CreateView):
    model = Reporter # código do professor
    form_class = ReporterForm # código do professor
    template_name = 'reporter/create.html' # código do professor
    success_url = reverse_lazy('relacionamentos:reporter_list_generic') # código do professor


class  ReporterUpdateViewGeneric(UpdateView):
    model = Reporter # código do professor
    # fields = '__all__' # código do professor
    form_class = ReporterForm # código do professor
    template_name = 'reporter/update.html' # código do professor
    success_url = reverse_lazy('relacionamentos:reporter_list_generic') # código do professor

    context_object_name = 'objeto_reporter'