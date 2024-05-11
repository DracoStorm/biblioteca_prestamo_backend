# Generated by Django 5.0.4 on 2024-05-11 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0006_admin_token_student_token'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Editorial',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=70)),
            ],
        ),
        migrations.AlterField(
            model_name='admin',
            name='token',
            field=models.CharField(default='5aab7e971f48cfbd53f9ab6d00911771f025c42df0c55d6567', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.category'),
        ),
        migrations.AlterField(
            model_name='book',
            name='editorial',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.editorial'),
        ),
    ]
