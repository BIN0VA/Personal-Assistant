# Generated by Django 5.1.2 on 2024-10-14 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pa_note', '0002_note_user'),
        ('pa_tag', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='note',
            name='tags',
            field=models.ManyToManyField(related_name='notes', to='pa_tag.tag'),
        ),
    ]
