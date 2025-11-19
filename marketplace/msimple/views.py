from django.shortcuts import render, redirect, get_object_or_404
from .models import Categoria, Producto, Cliente, Pedido
from .forms import CategoriaForm, ProductoForm, ClienteForm, PedidoForm

# Categoria

def listar_categorias(request):
    categorias = Categoria.objects.all()
    return render(request, 'categorias/listar.html', {'categorias': categorias})

def crear_categoria(request):
    form = CategoriaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_categorias')
    return render(request, 'categorias/form.html', {'form': form})

def editar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    form = CategoriaForm(request.POST or None, instance=categoria)
    if form.is_valid():
        form.save()
        return redirect('listar_categorias')
    return render(request, 'categorias/form.html', {'form': form})

def eliminar_categoria(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    return redirect('listar_categorias')

# Producto

def listar_productos(request):
    productos = Producto.objects.select_related('categoria').all()
    return render(request, 'productos/listar.html', {'productos': productos})

def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_productos')
    return render(request, 'productos/form.html', {'form': form})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('listar_productos')
    return render(request, 'productos/form.html', {'form': form})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, id=id)
    producto.delete()
    return redirect('listar_productos')

# Cliente

def listar_clientes(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/listar.html', {'clientes': clientes})

def crear_cliente(request):
    form = ClienteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/form.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        return redirect('listar_clientes')
    return render(request, 'clientes/form.html', {'form': form})

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    return redirect('listar_clientes')

# Pedido 

def listar_pedidos(request):
    pedidos = Pedido.objects.select_related('cliente', 'producto').all()
    return render(request, 'pedidos/listar.html', {'pedidos': pedidos})


def crear_pedido(request):
    form = PedidoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request, 'pedidos/form.html', {'form': form})

def editar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    form = PedidoForm(request.POST or None, instance=pedido)
    if form.is_valid():
        form.save()
        return redirect('listar_pedidos')
    return render(request, 'pedidos/form.html', {'form': form})

def eliminar_pedido(request, id):
    pedido = get_object_or_404(Pedido, id=id)
    pedido.delete()
    return redirect('listar_pedidos')

# Index

def index(request):
    total_categorias = Categoria.objects.count()
    total_productos = Producto.objects.count()
    total_clientes = Cliente.objects.count()
    total_pedidos = Pedido.objects.count()

    ultimos_productos = Producto.objects.order_by('-id')[:5]
    ultimos_pedidos = Pedido.objects.select_related('cliente', 'producto').order_by('-id')[:5]

    context = {
        'total_categorias': total_categorias,
        'total_productos': total_productos,
        'total_clientes': total_clientes,
        'total_pedidos': total_pedidos,
        'ultimos_productos': ultimos_productos,
        'ultimos_pedidos': ultimos_pedidos,
    }
    return render(request, 'index.html', context)
