from django.views import View
from relacionamentos.models.reporter import Reporter
from django.shortcuts import get_object_or_404, render, redirect


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