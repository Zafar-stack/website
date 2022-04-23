from django.db import models
from datetime import datetime

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    is_main = models.BooleanField()

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "категории"

    def __str__(self):
        return self.title


class Size(models.Model):
    title = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Размер"
        verbose_name_plural = "размеры"

    def __str__(self):
        return self.title


class Color(models.Model):
    title = models.CharField(max_length=300)
    code = models.CharField(max_length=300)

    class Meta:
        verbose_name = "Цвет"
        verbose_name_plural = "цвета"

    def __str__(self):
        return self.title


class Language(models.Model):
    title = models.CharField(max_length=200, default='')
    code = models.CharField(max_length=5, default='')

    class Meta:
        verbose_name = "Языки"
        verbose_name_plural = "языки"

    def __str__(self):
        return self.code


class Product (models.Model):
    title = models.CharField(max_length=300)
    reating = models.FloatField(default=0.0)
    views = models.IntegerField(default=0)
    old_price = models.IntegerField(default=0)
    new_price = models.IntegerField(default=0)
    short_description = models.TextField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    color = models.ForeignKey(Color, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    details = models.TextField()
    logo = models.ImageField(upload_to='upload')
    discount = models.IntegerField(default=0)
    is_new = models.BooleanField()
    is_best_saler = models.BooleanField()
    status = models.IntegerField(default=0)
    date = models.DateTimeField(default=None, blank=True, null=True)
    lang = models.ForeignKey(Language, on_delete=models.CASCADE, default=None, null=True)

    class Meta:
        verbose_name = "Товары"
        verbose_name_plural = "товары"

    def __str__(self):
        return self.title + ' ' + self.lang.code


class ProductImage(models.Model):
    title = models.CharField(max_length=300)
    logo = models.ImageField(upload_to='upload')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Фото товаров"
        verbose_name_plural = "фото товаров"

    def __str__(self):
        return self.title


class CommentItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    text = models.CharField(max_length=300)
    author_name = models.CharField(max_length=300)
    email = models.CharField(max_length=300)
    rating = models.IntegerField(default=0)
    pub_date = models.DateTimeField()

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "отзывы"

    def __str__(self):
        return self.text


class Cart(models.Model):
    title = models.CharField(max_length = 300, blank=True, default='')
    email = models.CharField(max_length = 300, blank=True, default='')
    last_name = models.CharField(max_length = 300, blank=True, default='')
    first_name = models.CharField(max_length = 300, blank=True, default='')
    zip_code = models.CharField(max_length = 300, blank=True, default='')
    country = models.CharField(max_length = 300, blank=True, default='')
    city = models.CharField(max_length = 300, blank=True, default='')
    person = models.CharField(max_length = 300, blank=True, default='')
    phone = models.CharField(max_length = 300, blank=True, default='')
    address = models.CharField(max_length = 300, blank=True, default='')
    is_accepted = models.BooleanField(default=False)
    payed = models.IntegerField(default=0)
    status = models.IntegerField(default=0)
    session_id = models.CharField(max_length=300, blank=True, default='')
    amount = models.FloatField(default=0)
    discount = models.FloatField(default=0)
    orig_price = models.FloatField(default=0)
    price = models.FloatField(default=0)

    class Meta:
        verbose_name = "Корзина"
        verbose_name_plural = "корзина"

    def __str__(self):
        return self.session_id


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    amount = models.FloatField(default=0)
    product_price = models.IntegerField(default=0)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    status = models.IntegerField(default=0)

    def product_prices(self):
        return f'{self.product} {self.product_price}'

    class Meta:
        verbose_name = "Карт айтемс"
        verbose_name_plural = "карт айтемс"

    def __str__(self):
        return self.product.title

    def name(self):
        return self.product_prices()


class Podpischiki(models.Model):
    email = models.CharField(max_length=200, default='')

    class Meta:
        verbose_name = "Подписчики"
        verbose_name_plural = "подписчики"

    def __str__(self):
        return self.email
