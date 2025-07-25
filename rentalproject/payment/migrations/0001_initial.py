# Generated by Django 5.2.4 on 2025-07-20 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('payment_method', models.CharField(max_length=50)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('paid_at', models.DateTimeField(auto_now_add=True)),
                ('payment_status', models.CharField(default='Unpaid', max_length=50)),
            ],
        ),
    ]
