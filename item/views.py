from django.shortcuts import render, get_object_or_404

from item.models import Item


# Create your views here.
def detail(request, item_id):
    item = get_object_or_404(Item, pk=item_id)
    related_items = Item.objects.filter(category=item.category, is_sold=False).exclude(
        pk=item_id
    )[0:4]
    return render(
        request, "item/detail.html", {
            "item": item,
            "related_items": related_items
        }
    )
