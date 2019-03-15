from django.views.generic import DetailView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse_lazy

from .models import Item, Category
from .forms import ItemForm, CategoryForm
from .mixins import AjaxableResponseMixin


class ItemCreateView(AjaxableResponseMixin, CreateView):
    form_class = ItemForm
    template_name = 'item_create_form.html'
    success_url = reverse_lazy('item_list')


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = 'item_update_form.html'
    success_url = reverse_lazy('item_list')


class ItemDeleteView(DeleteView):
    model = Item
    template_name = 'item_delete_confirm.html'
    success_url = reverse_lazy('item_list')


class ItemDetailView(DetailView):
    model = Item
    template_name = 'item_detail.html'


class ItemListView(ListView):
    model = Item
    template_name = 'item_list.html'
    context_object_name = 'items'


class CategoryCreateView(CreateView):
    form_class = CategoryForm
    template_name = 'category_create_form.html'
    success_url = reverse_lazy('item_list')
