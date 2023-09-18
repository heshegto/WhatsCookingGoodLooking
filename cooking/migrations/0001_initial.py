# Generated by Django 4.2.5 on 2023-09-18 22:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ReceiptStep',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('receipt_name', models.CharField(max_length=128)),
                ('step_number', models.PositiveSmallIntegerField(default=1)),
                ('required_elements', models.TextField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='product_images')),
                ('time_to_cook', models.TimeField()),
                ('is_last', models.BooleanField(default=True)),
                ('next_step', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='cooking.receiptstep')),
            ],
        ),
    ]
