# Generated by Django 5.1.6 on 2025-03-01 10:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EmpDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('emp_name', models.CharField(max_length=50)),
                ('emp_city', models.CharField(max_length=50)),
                ('emp_company', models.CharField(max_length=50)),
            ],
        ),
    ]
