from django.shortcuts import render_to_response,get_object_or_404,render
from django.template.context import RequestContext
from models import *
from django.http import HttpResponse,HttpResponseRedirect
from forms import *
from django.template.context import RequestContext
from django.contrib.auth.decorators import login_required
# Create your views here.
def home(request):
    categorias = Categoria.objects.all()
    enlaces = Enlace.objects.order_by("votos").all()
    template = "index.html"
    #return render_to_response(template,{"categorias" : categorias, "enlaces":enlaces})
    #return render_to_response(template,locals())
    return render(request,template,locals())

@login_required
def minus(request,id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos = enlace.votos - 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required
def plus(request,id_enlace):
	enlace = Enlace.objects.get(pk = id_enlace)
	enlace.votos = enlace.votos + 1
	enlace.save()
	return HttpResponseRedirect("/")

@login_required
def categoria(resquest,id_categoria):
	categorias = Categoria.objects.all()
	#cat =Categoria.objects.get(pk = id_categoria)
	cat = get_object_or_404(Categoria,pk = id_categoria)
	enlaces = Enlace.objects.filter(categoria = cat)
	template = "index.html"
	return render_to_response(template,locals())

@login_required
def add(request):
    categorias = Categoria.objects.all()
    if request.POST:
        form = EnlaceForm(request.POST)
        if form.is_valid():
            enlace = form.save(commit = False) #commit false es para que aun no se guarde el formulario
            enlace.usuario = request.user
            enlace.save()
            return HttpResponseRedirect("/")
    else:
        form = EnlaceForm()
    template = "form.html"
    return render_to_response(template,context_instance = RequestContext(request,locals()))