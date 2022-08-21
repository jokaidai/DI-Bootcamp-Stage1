# Generated by Django 4.1 on 2022-08-10 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gifs', '0002_alter_category_gif'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='gif',
            field=models.ManyToManyField(related_name='categories', to='gifs.gif'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]