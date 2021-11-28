# Generated by Django 3.2 on 2021-05-25 05:14

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order_info',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('store_name', models.CharField(default=1, max_length=30)),
                ('user', models.CharField(max_length=20, null=True)),
                ('rider_name', models.TextField(blank=True, null=True)),
                ('selected_food', models.TextField(blank=True, null=True)),
                ('order_price', models.TextField(blank=True, null=True)),
                ('delivery_fee', models.TextField(blank=True, null=True)),
                ('price_all', models.TextField(blank=True, null=True)),
                ('order_now', models.TextField(blank=True, max_length=10, null=True)),
                ('order_time', models.DateTimeField(default=datetime.datetime.now)),
            ],
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('store_name', models.CharField(max_length=50, null=True)),
                ('comment', models.TextField()),
                ('star', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('custom_img', models.ImageField(blank=True, null=True, upload_to='images')),
            ],
        ),
        migrations.CreateModel(
            name='Storekeepers',
            fields=[
                ('kakao_id', models.CharField(blank=True, max_length=30, null=True)),
                ('nickname', models.CharField(blank=True, max_length=20, null=True)),
                ('location', models.TextField(blank=True, null=True)),
                ('location_gps', models.TextField(blank=True, null=True)),
                ('store_notice', models.TextField(blank=True, null=True)),
                ('store_img', models.TextField(blank=True, null=True)),
                ('store_name', models.CharField(default=1, max_length=30, primary_key=True, serialize=False)),
                ('star', models.FloatField(blank=True, default=0, null=True)),
                ('review_count', models.IntegerField(blank=True, default=0, null=True)),
                ('order_count', models.IntegerField(blank=True, default=0, null=True)),
                ('Steamed_count', models.IntegerField(blank=True, default=0, null=True)),
                ('category_type', models.CharField(blank=True, max_length=16, null=True)),
                ('operation_time', models.CharField(max_length=50)),
                ('no_operation_time', models.CharField(max_length=50)),
                ('phone_number', models.CharField(max_length=20)),
                ('possible_delivery', models.CharField(blank=True, max_length=50, null=True)),
                ('delivery_fee', models.IntegerField(blank=True, null=True)),
                ('recommend', models.TextField(blank=True, null=True)),
                ('main', models.TextField(blank=True, null=True)),
                ('side', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kakao_id', models.CharField(default=1, max_length=30, null=True)),
                ('nickname', models.CharField(max_length=20, null=True)),
                ('location', models.TextField(null=True)),
                ('location_gps', models.TextField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
