from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.template.loader import render_to_string

from .models import Item, Category
from .forms import ItemForm, CategoryForm


def item_list(request):
    items = Item.objects.all()
    return render(request, 'catalog/item_list.html', {'items': items})


def save_item_form(request, form, template_name):
    data = dict()
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            data['form_is_valid'] = True
            items = Item.objects.all()
            data['html_item_list'] = render_to_string('catalog/includes/partial_item_list.html', {
                'items': items
            })
        else:
            data['form_is_valid'] = False
    context = {'form': form}
    data['html_form'] = render_to_string(
        template_name, context, request=request)
    return JsonResponse(data)


def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
    else:
        form = ItemForm()
    return save_item_form(request, form, 'catalog/includes/partial_item_create.html')


def item_update(request, pk):
    item = get_object_or_404(item, pk=pk)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=item)
    else:
        form = ItemForm(instance=item)
    return save_item_form(request, form, 'catalog/includes/partial_item_update.html')


def item_delete(request, pk):
    item = get_object_or_404(item, pk=pk)
    data = dict()
    if request.method == 'POST':
        item.delete()
        data['form_is_valid'] = True
        items = Item.objects.all()
        data['html_item_list'] = render_to_string('catalog/includes/partial_item_list.html', {
            'items': items
        })
    else:
        context = {'item': item}
        data['html_form'] = render_to_string(
            'catalog/includes/partial_item_delete.html', context, request=request)
    return JsonResponse(data)
