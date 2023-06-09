# Generated by Django 4.1.7 on 2023-05-15 16:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="product",
            name="category",
            field=models.ForeignKey(
                help_text="Категория курса.",
                on_delete=django.db.models.deletion.CASCADE,
                related_name="products",
                to="shop.category",
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="description",
            field=models.TextField(
                blank=True, help_text="Описание курса (опционально)."
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="image",
            field=models.ImageField(
                blank=True, help_text="Изображение.", upload_to="products/%Y/%m/%d"
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="name",
            field=models.CharField(
                db_index=True, help_text="Название курса.", max_length=200
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="price",
            field=models.DecimalField(
                decimal_places=2, help_text="Цена курса.", max_digits=10
            ),
        ),
        migrations.AlterField(
            model_name="product",
            name="stock",
            field=models.PositiveIntegerField(
                help_text="Доступное количество мест на курсе."
            ),
        ),
    ]
