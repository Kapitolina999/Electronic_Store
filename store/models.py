from django.db import models


class Location(models.Model):
    country = models.CharField(verbose_name='Страна', max_length=255)
    city = models.CharField(verbose_name='Город', max_length=255)
    street = models.CharField(verbose_name='Улица', max_length=255)
    number = models.PositiveSmallIntegerField(verbose_name='Номер дома')
    character = models.CharField(verbose_name='Литера', max_length=5, blank=True)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса'

    def __str__(self):
        return f'{self.country} {self.city} {self.street} {self.number} {self.character}'


class Product(models.Model):
    name = models.CharField(verbose_name='Наименование', max_length=255)
    model = models.CharField(verbose_name='Модель', max_length=255)
    date_release = models.DateField(verbose_name='Дата выхода на рынок')

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукция'

    def __str__(self):
        return f'{self.name} {self.model}'


class Store(models.Model):
    class Level(models.IntegerChoices):
        factory = 0, 'Завод'
        dealer = 1, 'Дилер'
        shop = 2, 'Розничный магазин'
        sole_proprietor = 3, 'ИП'

    name = models.CharField(verbose_name='Название', max_length=255, unique=True)
    email = models.EmailField(unique=True)
    location = models.ManyToManyField(Location, verbose_name='Адрес')
    created = models.DateField(verbose_name='Дата регистрации', auto_now_add=True)
    product = models.ManyToManyField(Product, verbose_name='Продукция', blank=True)
    level = models.PositiveSmallIntegerField(choices=Level.choices)
    supplier = models.ForeignKey('self', verbose_name='Поставщик', on_delete=models.SET_NULL, null=True, blank=True)
    debt = models.DecimalField(verbose_name='Задолженность', max_digits=12, decimal_places=2, blank=True, default=0.00)

    class Meta:
        verbose_name = 'Поставщик'
        verbose_name_plural = 'Поставщики'

    def __str__(self):
        return self.name



