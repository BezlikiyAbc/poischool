# Generated by Django 4.1.7 on 2023-05-16 15:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("shop", "0003_user_school"),
    ]

    operations = [
        migrations.AlterField(
            model_name="school",
            name="available",
            field=models.BooleanField(default=True, help_text="Прошла ли верификацию?"),
        ),
        migrations.AlterField(
            model_name="school",
            name="info",
            field=models.CharField(
                db_index=True, help_text="Информация о школе", max_length=9900
            ),
        ),
        migrations.AlterField(
            model_name="school",
            name="profile_pic",
            field=models.ImageField(
                blank=True, help_text="Аватарка школы", upload_to="profile_pic"
            ),
        ),
        migrations.AlterField(
            model_name="user",
            name="name",
            field=models.CharField(
                db_index=True, help_text="Имя пользователя", max_length=200
            ),
        ),
    ]
