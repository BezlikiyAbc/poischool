from django.db import models
from django.urls import reverse


class Category(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    slug = models.SlugField(max_length=200, db_index=True, unique=True)

    class Meta:
        ordering = ('name',)
        db_table = 'category'
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_list_by_category',
                       args=[self.slug])


class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,
                                 help_text="Категория курса.")
    name = models.CharField(max_length=200, db_index=True, help_text="Название курса.")
    slug = models.SlugField(max_length=200, db_index=True)
    description = models.CharField(max_length=77, blank=True, help_text="Краткое описание курса (опционально).")
    price = models.DecimalField(max_digits=10, decimal_places=2, help_text="Цена курса.")
    stock = models.PositiveIntegerField(help_text="Доступное количество мест на курсе.")
    available = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        index_together = (('id', 'slug'),)
        db_table = 'product'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('shop:product_detail',
                       args=[self.id, self.slug])


class User(models.Model):
    name = models.CharField(max_length=200, db_index=True, help_text="Имя пользователя")
    email = models.CharField(max_length=200, db_index=True, help_text="E-mail")
    password = models.CharField(max_length=50)
    slug = models.SlugField(max_length=200, db_index=True, blank=True)
    profile_pic = models.ImageField(upload_to='profile_pic',
                                    blank=True)
    API_Key = models.CharField(max_length=255, unique=True, blank=True, null=True, verbose_name='Токен')

    class Meta:
        db_table = 'users'
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.name


class School(models.Model):
    name = models.CharField(max_length=900, db_index=True, help_text="Название школы (образовательной организации)")
    info = models.CharField(max_length=900, db_index=True, help_text="Информация о школе")
    profile_pic = models.ImageField(upload_to='profile_pic', help_text="Аватарка школы",
                                    blank=True)
    file = models.FileField(upload_to='products/%Y/%m/%d', blank=True, help_text="Скан подтверждающего документа")
    available = models.BooleanField(default=True, help_text="Прошла ли верификацию?")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'school'
        verbose_name = 'School'
        verbose_name_plural = 'Schools'


class CourseSchool(models.Model):
    product = models.ForeignKey(Product, related_name='course_products', on_delete=models.CASCADE, help_text="Продукт")
    school = models.ForeignKey(School, related_name='course_schools', on_delete=models.CASCADE, help_text="Школа")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.product} - {self.school}"

    class Meta:
        db_table = 'courseschools'
        verbose_name = 'CourseSchool'
        verbose_name_plural = 'CourseSchools'
        unique_together = ("product", "school")


class Basket(models.Model):
    product = models.ForeignKey(Product, related_name='basket_products', on_delete=models.CASCADE, help_text="Продукт")
    user = models.ForeignKey(User, related_name='basket_users', on_delete=models.CASCADE, help_text="Пользователь")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Дата обновления')

    def __str__(self):
        return f"{self.product} - {self.user}"

    class Meta:
        db_table = 'baskets'
        verbose_name = 'Basket'
        verbose_name_plural = 'Baskets'
        unique_together = ("product", "user")
