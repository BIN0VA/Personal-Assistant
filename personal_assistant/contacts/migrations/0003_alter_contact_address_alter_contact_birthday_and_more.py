# Generated by Django 5.1.1 on 2024-10-04 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_alter_contact_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='address',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='birthday',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='email',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
