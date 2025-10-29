import string

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


class ReporterGerarCodigoView(View):
    @staticmethod
    def get(request,reporter_id):
        reporter = get_object_or_404(Reporter, pk=reporter_id)
        try:
            letters = string.ascii_letters + string.digits
            reporter.name = ''.join(random.choice(letters) for i in range(10))
            reporter.save()
            return redirect('relacionamentos:reporter')

        except Exception as e:
            print(e)
            return render(request, "reporter/list.html")

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