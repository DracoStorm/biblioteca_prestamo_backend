# Generated by Django 5.0.4 on 2024-05-08 00:21

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admin',
            fields=[
                ('register', models.PositiveIntegerField(default=100000000, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999)])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=60)),
                ('last_session', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('author', models.CharField(max_length=50)),
                ('category', models.CharField(choices=[('Terror', 'TERROR'), ('Fantasía', 'FANTASIA'), ('Ciencias de la computación', 'CS'), ('Químico Farmaco-biología', 'QFB')], max_length=50)),
                ('editorial', models.CharField(choices=[('Alfa Omega', 'C1'), ('Porrua', 'C2'), ('Fondo cultural', 'C3')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Loan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_date', models.DateField(auto_now_add=True)),
                ('devolution_date', models.DateField()),
                ('renew_tries', models.IntegerField(default=0)),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='modelo.book')),
            ],
        ),
        migrations.CreateModel(
            name='StudentLoans',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('loan_0', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_0', to='modelo.loan')),
                ('loan_1', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_1', to='modelo.loan')),
                ('loan_2', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_2', to='modelo.loan')),
                ('loan_3', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_3', to='modelo.loan')),
                ('loan_4', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_4', to='modelo.loan')),
                ('loan_5', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_5', to='modelo.loan')),
                ('loan_6', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_6', to='modelo.loan')),
                ('loan_7', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_7', to='modelo.loan')),
                ('loan_8', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_8', to='modelo.loan')),
                ('loan_9', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='loan_9', to='modelo.loan')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('register', models.PositiveIntegerField(default=100000000, primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(100000000), django.core.validators.MaxValueValidator(999999999)])),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('e_mail', models.EmailField(max_length=60)),
                ('loans', models.ForeignKey(default='NULL', null=True, on_delete=django.db.models.deletion.SET_NULL, to='modelo.studentloans')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]