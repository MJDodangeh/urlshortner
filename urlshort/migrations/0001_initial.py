# Generated by Django 4.1.5 on 2023-01-19 18:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='urlShortener',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('longurl', models.CharField(max_length=255)),
                ('shorturl', models.CharField(max_length=10, null=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='userurl', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
