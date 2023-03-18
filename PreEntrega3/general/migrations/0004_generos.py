# Generated by Django 4.1.7 on 2023-03-18 15:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0003_autores'),
    ]

    operations = [
        migrations.CreateModel(
            name='generos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Ingrese el nombre del género (ej: Ciencia Ficción, Poesía, Fantasía, etc)', max_length=100)),
            ],
        ),
    ]
