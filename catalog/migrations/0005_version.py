# Generated by Django 4.2.7 on 2023-12-22 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='Version',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version_number', models.IntegerField(default=1, verbose_name='version_number')),
                ('version_name', models.CharField(max_length=50, verbose_name='version_name')),
                ('is_active', models.BooleanField(default=True, verbose_name='is_active')),
                ('product', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.product', verbose_name='product')),
            ],
            options={
                'verbose_name': 'version',
                'verbose_name_plural': 'versions',
            },
        ),
    ]
