# Generated by Django 4.2.1 on 2023-05-16 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0010_alter_school_info'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='school',
            name='image',
        ),
        migrations.AddField(
            model_name='school',
            name='file',
            field=models.FileField(blank=True, help_text='Скан подтверждающего документа', upload_to='products/%Y/%m/%d'),
        ),
    ]
