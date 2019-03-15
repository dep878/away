from django.forms import ModelForm
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Div, HTML, Field, Fieldset, ButtonHolder
from crispy_forms.bootstrap import FieldWithButtons, StrictButton
# from django.forms.models import inlineformset_factory
from .models import Item, Category


class ItemForm(forms.ModelForm):
    # title = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'','class': "form-control"}), label=(u'Название'))

    class Meta:
        model = Item
        fields = '__all__'
        exclude = ['slug', 'code', 'price_purchase_rub',
                   'created_at', 'updated_at', ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.fields['category'].label = False
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
                # Div('category', css_class='input-group'),
                FieldWithButtons('category', StrictButton(
                    "Go!", css_class='btn-outline-success', css_id='123', data_toggle='modal', data_target='#ModalCategory'),
                    css_class='form-group col-md-6 mb-0'),
                # Div(
                #     Field('category', wrapper_class='form-control'),
                #     HTML('''
                #         <span class="input-group-append">
                #             <a href="{% url 'category_add' %}" class="btn btn-outline-success">Add</a>
                #         </span>
                #         '''),
                #     css_class='input-group'
                # ),

                #                 <div class="input-group mb-3">
                #   <input type="text" class="form-control" placeholder="Recipient's username" aria-label="Recipient's username" aria-describedby="basic-addon2">
                #   <div class="input-group-append">
                #     <button class="btn btn-outline-secondary" type="button">Button</button>
                #   </div>
                # </div>



                # Column('category', css_class='input-group col-md-4 mb-0'),
                # Submit('submit', 'Сохранить',
                #        css_class='form-group col-md-2 mb-0'),
                # Div(HTML('''
                # <span class="input-group-btn">
                #     <button type="button" class="btn btn-outline-success">Success</button>
                # </span>
                # '''),
                #     css_class='input-group'),
                css_class='form-row'
            ),
            Row(
                Column('size_height', css_class='form-group col-md-2 mb-0'),
                Column('size_width', css_class='form-group col-md-2 mb-0'),
                Column('size_length', css_class='form-group col-md-2 mb-0'),
                Column('size_diameter', css_class='form-group col-md-3 mb-0'),
                Column('weight', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('country_origin', css_class='form-group col-md-3 mb-0'),
                Column('period', css_class='form-group col-md-2 mb-0'),
                Column('style', css_class='form-group col-md-2 mb-0'),
                Column('material', css_class='form-group col-md-2 mb-0'),
                Column('condition', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'description',
            Row(
                Column('date_purchase', css_class='form-group col-md-2 mb-0'),
                Column('city_purchase', css_class='form-group col-md-4 mb-0'),
                Column('price_purchase', css_class='form-group col-md-2 mb-0'),
                Column('exchange_rate', css_class='form-group col-md-2 mb-0'),
                Column('additional_expenses',
                       css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            Row(
                Column('price_selling', css_class='form-group col-md-3 mb-0'),
                Column('date_prepayment', css_class='form-group col-md-3 mb-0'),
                Column('sum_prepayment', css_class='form-group col-md-3 mb-0'),
                Column('date_delivery', css_class='form-group col-md-3 mb-0'),
                css_class='form-row'
            ),
            'client',
            Submit('submit', 'Сохранить')
        )


# class ImageForm(ModelForm):
#     class Meta:
#         model = Image
#         fields = ('file', )


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Row(
                Column('title', css_class='form-group col-md-6 mb-0'),
            ),
            Submit('submit', 'Сохранить')
        )


# ImageFormSet = inlineformset_factory(Item, Image, form=ImageForm, extra=1)
