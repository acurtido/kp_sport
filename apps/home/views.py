from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import redirect
from .forms import ActividadEdicionForm, ActividadForm, ActividadCreacionForm, EncuentroCreacionForm
from .models import Jugador, Actividad, Encuentro
from emoji import Emoji

@login_required(login_url="/login/")
def index(request):
    encuentros = Encuentro.objects.all().order_by('-fecha', '-hora')
    context = {'segment': 'encuentros', "encuentros": encuentros}
    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def crear_encuentro(request):
    form = EncuentroCreacionForm()
    if request.method == "POST" and "submit_guardar" in request.POST:
        form = EncuentroCreacionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.jugador_creador = Jugador.objects.get(pk=request.user.id)
            form.save()
            return redirect('actualizar-encuentro', pk=obj.id)
    elif request.method == "POST" and "submit_cancelar" in request.POST:
            return redirect('/')
    context = {'form': form}
    html_template = loader.get_template('base/encuentro_form.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def actualizar_encuentro(request, pk):
    encuentro = Encuentro.objects.get(pk=pk)
    form = EncuentroCreacionForm(instance=encuentro)
    if request.method == "POST" and "submit_guardar" in request.POST:
        form = EncuentroCreacionForm(request.POST, instance=encuentro)
        if form.is_valid():
            form.save()
            return redirect('actualizar-encuentro', pk=encuentro.id )
    elif request.method == "POST" and "submit_cancelar" in request.POST:
            return redirect('/')
    context = {"form": form}
    html_template = loader.get_template('base/encuentro_form.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def listar_actividades(request):
    context = {"actividades": Actividad.objects.all().order_by('-id'), "segment": "actividades"}
    html_template = loader.get_template('base/actividad_lista.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def ver_actividad(request, pk):
    context = {"actividad": Actividad.objects.get(pk=pk)}
    html_template = loader.get_template('base/actividad.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def crear_actividad(request):
    form = ActividadCreacionForm()
    if request.method == "POST":
        form = ActividadCreacionForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.jugador_creador = Jugador.objects.get(pk=request.user.id)
            form.save()
            return redirect('/actividades')
    context = {'form': form}
    html_template = loader.get_template('base/actividad_form.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def actualizar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    form = ActividadEdicionForm(instance=actividad)
    if request.method == "POST":
        form = ActividadEdicionForm(request.POST, instance=actividad)
        if form.is_valid():
            form.save()
            return redirect('/actividades')
    context = {"form": form}
    html_template = loader.get_template('base/actividad_form.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def eliminar_actividad(request, pk):
    actividad = Actividad.objects.get(pk=pk)
    context = {"obj": actividad}
    if request.method == "POST":
        actividad.delete()
        return redirect('dashboard.html')
    html_template = loader.get_template('base/actividad_eliminar.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
