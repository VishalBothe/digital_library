# Generated by Django 3.2.4 on 2021-06-11 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_customuser_last_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='due_date',
            field=models.DateField(),
        ),
    ]