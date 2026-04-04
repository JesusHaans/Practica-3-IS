from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Pedido

# Create your views here.
def home(request):
    return render(request, "home.html")

def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()

    return render(request, "users/register.html", {"form": form})


@login_required
def dashboard(request):
    return render(request, "dashboard.html")

@login_required
def lista_pedidos(request):
    pedidos = Pedido.objects.filter(usuario=request.user).order_by("-fecha_creacion")
    context = {"pedidos":pedidos}
    return render(request, "core/lista_pedidos.html", context)

@login_required
def  detalle_pedido(request, pedido_id):
    pedido  = get_object_or_404(Pedido, id = pedido_id, usuario = request.user)
    context = {"pedido":pedido}
    return render(request, "core/detalle_pedido.html",context)
