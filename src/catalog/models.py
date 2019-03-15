import uuid
from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.urls import reverse
from django.db.models import F


class Item(models.Model):
    title = models.CharField(max_length=255, verbose_name='Название товара')
    slug = models.SlugField(max_length=255, unique=True)
    code = models.CharField(max_length=255)
    date_purchase = models.DateField(
        auto_now=False, auto_now_add=False, verbose_name='Дата покупки')
    category = models.ForeignKey(
        'Category', on_delete=models.CASCADE, verbose_name='Категория')
    country_origin = models.CharField(
        max_length=255, verbose_name='Страна производства')
    material = models.CharField(max_length=255, verbose_name='Материал')
    size_height = models.IntegerField(
        blank=True, null=True, verbose_name='Высота')
    size_width = models.IntegerField(
        blank=True, null=True, verbose_name='Ширина')
    size_length = models.IntegerField(
        blank=True, null=True, verbose_name='Длина')
    size_diameter = models.IntegerField(
        blank=True, null=True, verbose_name='Диаметр')
    style = models.CharField(max_length=255, blank=True, verbose_name='Стиль')
    period = models.CharField(max_length=255, verbose_name='Период')
    condition = models.CharField(
        max_length=255, blank=True, verbose_name='Состояние товара')
    description = models.TextField(blank=True, verbose_name='Описание товара')
    # file = models.FileField(upload_to='images/')
    # uploaded_at = models.DateTimeField(auto_now_add=True)
    city_purchase = models.CharField(
        max_length=255, verbose_name='Город покупки')
    weight = models.DecimalField(
        max_digits=5, decimal_places=2, blank=True, null=True, verbose_name='Вес')
    price_purchase = models.IntegerField(verbose_name='Цена покупки, €')
    price_purchase_rub = models.IntegerField(blank=True, null=True)
    additional_expenses = models.IntegerField(
        blank=True, default=0, verbose_name='Доп. расходы')
    exchange_rate = models.DecimalField(
        max_digits=5, decimal_places=2, verbose_name='Курс обмена')
    price_selling = models.IntegerField(verbose_name='Цена продажи, ₽')
    client = models.TextField(blank=True, verbose_name='Данные покупателя')
    sum_prepayment = models.IntegerField(
        blank=True, null=True, verbose_name='Сумма предоплаты')
    date_prepayment = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Дата предоплаты')
    date_delivery = models.DateField(
        auto_now=False, auto_now_add=False, blank=True, null=True, verbose_name='Дата доставки')
    sold = models.BooleanField(verbose_name='Товар продан')
    publish = models.BooleanField(verbose_name='Опубликовать')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def get_absolute_url(self):
        # return reverse('item_detail', kwargs={'pk': self.pk})
        return reverse('item_detail', kwargs=[str(self.slug)])
        # args=[str(self.slug)])

    def __str__(self):
        return self.title

    def _update_price_purchase_rub(self, created=False):
        if created:
            Item.objects.filter(code=self.code).update(price_purchase_rub=F(
                'price_purchase') * F('exchange_rate') + F('additional_expenses'))

    def save(self, *args, **kwargs):
        created = self.pk is None
        if not self.id:
            self.code = 'AW' + \
                self.date_purchase.strftime(
                    "%y%m") + str(uuid.uuid4()).upper()[:5]
            slug = slugify(self.code)
            self.slug = slug
            super(Item, self).save(*args, **kwargs)
        else:
            self.slug = self.slug
            super(Item, self).save(*args, **kwargs)
        self._update_price_purchase_rub(created)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         self.price_purchase_rub = self.price_purchase * \
    #             self.exchange_rate + self.additional_expenses
    #         super(Item, self).save(*args, **kwargs)
    #     else:
    #         self.slug = self.slug
    #         super(Item, self).save(*args, **kwargs)

#         date = timezone.now().date()
# print date.strftime("%Y/%m/%d")

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title, 'ru')
    #     self.slug = slug
    #     super(Item, self).save(*args, **kwargs)

        # code = "cid_%" % (self.pk)

    # def save(self, *args, **kwargs):
    #     if not self.slug:
    #         slug=slugify(self.title, 'ru')
    #         self.slug = slug
    #         super(Item, self).save(*args, **kwargs)
    #     else:
    #         self.slug = self.slug
    #         super(Item, self).save(*args, **kwargs)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.slug)
    #     super(Item, self).save(*args, **kwargs)

    # def slug(self):
    #     return slugify(self.title)

    # def save(self, *args, **kwargs):
    #     self.slug = slugify(self.title)
    #     return super(Item, self).save(*args, **kwargs)

    # def get_image_filename(instance, filename):
    #     title = instance.item.title
    #     slug = slugify(title)
    #     return "item_images/%s-%s" % (slug, filename)


# class Image(models.Model):
#     item = models.ForeignKey(Item, default=None)
#     image = models.ImageField(upload_to=get_image_filename, verbose_name='Image')

# class Image(models.Model):
#     item = models.ForeignKey('Item', on_delete=models.CASCADE)
#     file = models.FileField(upload_to="images")


class Category(models.Model):
    title = models.CharField(
        max_length=255, unique=True, verbose_name='Название')

    def __str__(self):
        return self.title
