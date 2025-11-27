import string
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import View
from relacionamentos.models.reporter import Reporter
from django.shortcuts import get_object_or_404, render, redirect
import random


class ReporterView(View):

    @staticmethod
    def get(request):
        reporters = Reporter.objects.all()
        context = {'reporters': reporters}
        return render(request, "reporter/list.html", context)


class ReporterDetailView(View):
    @staticmethod
    def get(request,pk):
        reporter = Reporter.objects.get(id=pk)
        context = {"reporter": reporter}
        return render(request, "reporter/read.html", context)


class ReporterGerarCodigoView(LoginRequiredMixin,  PermissionRequiredMixin, View ):
    login_url = 'accounts:login'
    permission_required = 'relacionamentos.generate_code_reporter'
    @staticmethod
    def get(request, pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            letters = string.ascii_letters +string.digits
            reporter.cod = "".join(random.choice(letters) for i in range(10))
            reporter.save()
            return redirect('relacionamentos:reporter_view_generate_code')
        except:
            print(f"Erro ao gerar código para reporter {reporter}")
            return redirect('relacionamentos:reporter')
        

class ReporterDeleteView(View):
    @staticmethod
    def get(request,pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            context = {"reporter": reporter}
            return render(request, "reporter/delete.html", context)
        except Exception as e:
            context= {}
            print(e)
            return render(request, "reporter/list.html",context)

    @staticmethod
    def post(request,pk):
        reporter = get_object_or_404(Reporter, pk=pk)
        try:
            v_reporter_id = request.POST.get("v_reporter_id",None)
            if int(v_reporter_id) == pk:
                reporter.delete()
                return redirect('relacionamentos:reporter')
        except Exception as e:
            context = {}
            print(e)
            return render(request, "reporter/list.html",context)