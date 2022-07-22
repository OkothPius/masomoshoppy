from django.db import models
from django.urls import reverse

class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #     return reverse('shop:product_list_by_category', args=[self.slug])

class Type(models.Model):
    name = models.CharField(max_length=200, null=True)

    class Meta:
        ordering = ('name',)
        verbose_name = 'type'
        verbose_name_plural = 'types'

    def __str__(self):
        return self.name

class Book(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Stationary(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Uniform(models.Model):
    UNIFORM_SIZES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'Extra Large'),
    )
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    uniform_size = models.CharField(max_length=2, choices=UNIFORM_SIZES)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Electronic(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name


class Equipment(models.Model):
    category = models.ForeignKey(Category, related_name='products',
                                 on_delete=models.CASCADE)
    type = models.ForeignKey(Type, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    description = models.TextField(blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)

    def __str__(self):
        return self.name

# class Review(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     product = models.ForeignKey(Product , on_delete=models.CASCADE)
#     date = models.DateTimeField(auto_now_add=True)
#     text = models.TextField(max_length=3000 , blank=True)
#     rate = models.PositiveSmallIntegerField(choices=RATE_CHOICES)
#     likes= models.PositiveIntegerField(default=0)
#     dislikes = models.PositiveIntegerField(default=0)
#
#     def __str__(self):
#         return self.user.full_name
