from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from django.http import HttpResponse, Http404, HttpResponseRedirect

from .models import Item
from .forms import DelForm, ItemForm

import csv

def index(request):
    if request.method == "POST":
        if "createItem" in request.POST:
            form = ItemForm(request.POST)
            if form.is_valid():
                newItem = Item(itemName=form.data["itemName"], itemDesc=form.data["itemDesc"], numItems=form.data["numItems"])
                newItem.save()

        if "delete" in request.POST:
            form = DelForm(request.POST)
            item = Item.objects.get(pk=form.data["id"])
            item.delete()
        return redirect("./")

    itemList = Item.objects.order_by('id')
    context = {'itemList': itemList}
    return render(request, 'inventoryapp/index.html', context)

def itemView(request, item_id):
    try:
        item = Item.objects.get(pk=item_id)
        if request.method == "POST":
            form = ItemForm(request.POST)
            if form.is_valid():
                item.itemName=form.data["itemName"]
                item.itemDesc=form.data["itemDesc"]
                item.numItems=form.data["numItems"]
                item.save()
            return redirect("/inventoryapp/")
        else:
            form = ItemForm(instance=item)
    except Item.DoesNotExist:
        raise Http404("Item does not exist")
    return render(request, 'itemView/index.html', {'form': form})

def exportCSV(request):
    response = HttpResponse(content_type="text/csv")
    writer = csv.writer(response)
    writer.writerow(["id", "itemName", "itemDesc", "numItems"])
    for item in Item.objects.all().values_list("id", "itemName", "itemDesc", "numItems"):
        writer.writerow(item)
    response["Content-Disposition"] = "attachment; filename=inventory.csv"
    return response