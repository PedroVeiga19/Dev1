import string

from relacionamentos.models.reporter import Reporter
from relacionamentos.forms.reporter_form import ReporterForm
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth.decorators import login_required,permission_required
from django.views.decorators.http import require_http_methods
import random

@login_required(login_url='/login/')
@permission_required("usuario.can_list_reporter")
def reporter_list(request):
    reporters = Reporter.objects.all()
    context = {"reporters":reporters}
    return render(request, "reporter/list.html", context) 

@require_http_methods(['GET'])
def reporter_detail(request,pk):    
    reporter = Reporter.objects.get(id=pk)
    context = {"reporter":reporter}
    return render(request, "reporter/read.html", context)

@require_http_methods(['GET'])
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


@require_http_methods(['GET'])
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

@require_http_methods(['GET'])
def create(request):
    if request.method == "POST":
        form = ReporterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter')

    else:
        form = ReporterForm()

    context = {
        'form':form,
    }

    return render(request,'reporter/create.html',context)

@require_http_methods(['GET'])
def update(request,reporter_id):
    reporter = get_object_or_404(Reporter, pk=reporter_id)
    if request.method == "POST":
        form = ReporterForm(request.POST,instance=reporter)
        if form.is_valid():
            form.save()
            return redirect('relacionamentos:reporter')

    else:
        form = ReporterForm(instance=reporter)

    context = {
        'form': form,
        'reporter':reporter,
    }

    return render(request, 'reporter/update.html', context)
