# Generated by Django 5.0.4 on 2024-05-11 08:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0007_category_editorial_alter_admin_token_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='admin',
            name='token',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]