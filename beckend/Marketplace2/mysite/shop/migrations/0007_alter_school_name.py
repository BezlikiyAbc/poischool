# Generated by Django 4.2.1 on 2023-05-16 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_remove_product_image_remove_product_updated_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='school',
            name='name',
            field=models.CharField(db_index=True, help_text='Название школы (образовательной организации)', max_length=900),
        ),
    ]
