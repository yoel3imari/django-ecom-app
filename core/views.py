from django.shortcuts import render

from item.models import Item, Category
from .forms import SignUpForm

# Create your views here.
def index(request):
    items = Item.objects.filter(is_sold=False)[0:6]
    categories = Category.objects.all()

    return render(request, "core/index.html", {
        'items': items,
        'categories': categories
    })

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})