import string

from relacionamentos.models.reporter import Reporter
from django.shortcuts import get_object_or_404, render, redirect
import random


def reporter_list(request):
    reporters = Reporter.objects.all()
    context = {"reporters":reporters}
    return render(request, "reporter/list.html", context) 

def reporter_detail(request,pk):    
    reporter = Reporter.objects.get(id=pk)
    context = {"reporter":reporter}
    return render(request, "reporter/read.html", context)

def reporter_delete(request,pk):    
    reporter = get_object_or_404(Reporter, pk=pk)
    try:
        if request.method == "POST":
            v_reporter_id = request.POST.get("reporter_id",None)
            if int(v_reporter_id) == reporter.id:
                reporter.delete()
                return redirect('relacionamentos:reporter')
        else:
            context ={'reporter': reporter}
    except Exception as e:
        context = {}
        print(e)
        return render(request, "reporter/list.html", context) 

    return render(request, "reporter/delete.html", context)


def reporter_gerar_codigo(request,reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    try:
        letters = string.ascii_letters + string.digits
        reporter.name = ''.join(random.choice(letters) for i in range(10))
        reporter.save()
        return redirect('relacionamentos:reporter')

    except Exception as e:
        print(e)
        return render(request, "reporter/list.html")
