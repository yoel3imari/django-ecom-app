from django.shortcuts import render, get_object_or_404

from item.models import Item
# Create your views here.
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    return render(request, "item/detail.html", {"item": item})