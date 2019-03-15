from django.http import HttpResponseRedirect
from django.views.generic import ListView, CreateView, UpdateView, TemplateView, DetailView
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from django.shortcuts import render
from django.http import JsonResponse
from django.views import View

from .models import Item, Category
from .forms import ItemForm, CategoryForm

# class ItemModelList(TemplateView):
#     template_name = 'catalog.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context = Item.objects.all()
#         return context


class ItemModelList(ListView):
    template_name = 'catalog.html'
    model = Item
    context_object_name = 'items'

    # context_object_name = 'my_book_list'   # ваше собственное имя переменной контекста в шаблоне
    # queryset = Book.objects.filter(title__icontains='war')[:5] # Получение 5 книг, содержащих слово 'war' в заголовке
    # template_name = 'books/my_arbitrary_template_name_list.html'  # Определение имени вашего шаблона и его расположения

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['item'] = Item.objects.all()
    #     return context


class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'item_add.html'
    # model = Item
    success_url = reverse_lazy('catalog')

    def get(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        return self.render_to_response(
            self.get_context_data(form=form))

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))

# OLD
#     def get(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         return self.render_to_response(
#             self.get_context_data(form=form))

#     def post(self, request, *args, **kwargs):
#         self.object = None
#         form_class = self.get_form_class()
#         form = self.get_form(form_class)
#         if (form.is_valid()):
#             return self.form_valid(form)
#         else:
#             return self.form_invalid(form)

#     def form_valid(self, form):
#         self.object = form.save()
#         return HttpResponseRedirect(self.get_success_url())

#     def form_invalid(self, form):
#         return self.render_to_response(
#             self.get_context_data(form=form))


class ItemUpdateView(UpdateView):
    template_name = 'item_add.html'
    model = Item
    form_class = ItemForm

    def get_success_url(self):
        self.reverse_lazy('catalog')
        return self.success_url

    def get_context_data(self, **kwargs):
        context = super(ItemUpdateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context['form'] = RecipeForm(
                self.request.POST, instance=self.object)
        else:
            context['form'] = RecipeForm(instance=self.object)
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        if (form.is_valid()):
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())

    def form_invalid(self, form):
        return self.render_to_response(
            self.get_context_data(form=form))


class ItemDetailView(DetailView):
    model = Item


class CategoryCreateView(CreateView):
    template_name = 'category_add.html'
    model = Category
    form_class = CategoryForm
    success_url = reverse_lazy('catalog')


class CategoryUpdateView(UpdateView):
    template_name = 'category_add.html'
    model = Category
    form_class = CategoryForm
