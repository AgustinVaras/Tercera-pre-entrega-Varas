# Generated by Django 4.1.7 on 2023-03-17 00:54

from django.db import migrations, models
import general.models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('general', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=120, unique=True)),
                ('telefono', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region='AR')),
            ],
            bases=(models.Model, general.models.Persona),
        ),
    ]
