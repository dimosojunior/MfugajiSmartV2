# Generated by Django 4.2.6 on 2024-06-09 10:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductsCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ordered', models.BooleanField(default=False)),
                ('total_price', models.FloatField(default=0, verbose_name='Total Price')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products  Cart',
            },
        ),
        migrations.CreateModel(
            name='ProductsCategories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CategoryName', models.CharField(max_length=100, verbose_name='Category Name')),
                ('Store', models.IntegerField(blank=True, null=True, verbose_name='Quantity in Store')),
                ('CategoryImage', models.ImageField(blank=True, null=True, upload_to='media/Images/', verbose_name='Category Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Products Categories',
            },
        ),
        migrations.CreateModel(
            name='ProductsOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_price', models.FloatField(verbose_name='Total Price')),
                ('CategoryId', models.IntegerField(blank=True, null=True, verbose_name='Category ID')),
                ('closed_order_state', models.BooleanField(blank=True, default=False, null=True, verbose_name='Is Order Closed ?')),
                ('order_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('cart', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.productscart')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products Orders',
            },
        ),
        migrations.CreateModel(
            name='ProductsUnit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Unit', models.CharField(max_length=500, verbose_name='Unit')),
                ('Description', models.TextField(blank=True, max_length=500, null=True, verbose_name='Description')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name_plural': 'Products Unit',
            },
        ),
        migrations.CreateModel(
            name='ProductsStores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, verbose_name='Product Name')),
                ('product_second_name', models.CharField(blank=True, default='', max_length=100, null=True, verbose_name='Product Second Name')),
                ('price', models.CharField(blank=True, max_length=20, null=True)),
                ('ProductQuantity', models.IntegerField(blank=True, null=True, verbose_name='Product Quantity')),
                ('InitialProductQuantity', models.IntegerField(blank=True, null=True, verbose_name='Initial Product Quantity')),
                ('ProductImage', models.ImageField(blank=True, null=True, upload_to='media/ProductsInventoryImages/', verbose_name='Product Image')),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('Unit', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.productsunit', verbose_name='Product Unit')),
                ('productCategory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.productscategories', verbose_name='Product Category')),
            ],
            options={
                'verbose_name_plural': 'Stores',
            },
        ),
        migrations.CreateModel(
            name='ProductsOrderItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('order_status', models.BooleanField(blank=True, default=False, null=True, verbose_name='Status')),
                ('quantity', models.IntegerField(default=1)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productsorder')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productsstores')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products Orders Items',
            },
        ),
        migrations.AddField(
            model_name='productscategories',
            name='Unit',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.productsunit', verbose_name='Product Unit'),
        ),
        migrations.CreateModel(
            name='ProductsCartItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0)),
                ('quantity', models.IntegerField(default=1)),
                ('Created', models.DateTimeField(auto_now_add=True)),
                ('Updated', models.DateTimeField(auto_now=True)),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productscart')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='App.productsstores')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Products  Cart Items',
            },
        ),
    ]
