# Generated by Django 5.0.4 on 2024-05-08 04:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelo', '0004_alter_studentloans_loan_0_alter_studentloans_loan_1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='loans',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='modelo.studentloans'),
            preserve_default=False,
        ),
    ]
