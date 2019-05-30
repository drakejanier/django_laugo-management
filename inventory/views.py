from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'index.html')

def inventory(request):
    return render(request, 'inventory.html')

def display_items(request):
    items = Item.objects.all()
    context = {
        'items' : items,        
    }
    return render(request, 'inventory.html', context)

def add_Item(request):
    if request.method == "POST":
        form = InventoryFrm(request.POST)

        if form.is_valid(): #validate the form
            form.save()
            return redirect('inventory')
    else:
        form = InventoryFrm()
        return render(request, 'add_new.html', {'form':InventoryFrm})

def edit_inventory(request, pk):
    itemE = get_object_or_404(Item, pk=pk) #get form Item model with primary key

    if request.method == "POST":
        form = InventoryFrm(request.POST, instance=itemE)
        if form.is_valid():
            form.save()
            return redirect('display_items')

    else: #IF GET
        form = InventoryFrm(instance=itemE)

        return render(request, 'edit_item.html', {'form': form})
        

def delete_inventory(request, pk):
    Item.objects.filter(id=pk).delete()

    itemsD = Item.objects.all()

    context = {
        'items': itemsD
    }

    return render(request, 'display_item', context)
