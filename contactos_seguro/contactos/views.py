from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Contacto
from .forms import ContactoForm


@login_required
def lista_contactos(request):
    contactos = Contacto.objects.filter(usuario=request.user)
    form = ContactoForm()        
    if request.method == 'POST':
        form = ContactoForm(request.POST)
        if form.is_valid():
            contacto = form.save(commit=False)
            contacto.usuario = request.user
            contacto.save()
            return redirect('lista')
    return render(request, 'contactos/lista.html', {'contactos': contactos, 'form': form})

@login_required
def editar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id, usuario=request.user)
    if request.method == 'POST':
        form = ContactoForm(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            return redirect('lista')
    return redirect('lista')

@login_required
def eliminar_contacto(request, id):
    contacto = get_object_or_404(Contacto, id=id)
    contacto.delete()
    return redirect('lista')

def cerrar_sesion(request):
    logout(request) 
    return redirect('login')  