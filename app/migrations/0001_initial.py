# Generated by Django 4.0 on 2023-01-18 08:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('state', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Maharashtra', 'Maharashtra'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('West Bengal', 'West Bengal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('description', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('M', 'Mobile'), ('L', 'Laptop'), ('TW', 'Top Wear'), ('BW', 'Bottom Wear')], max_length=2)),
                ('Product_image', models.ImageField(upload_to='producting')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jammu and Kashmir', 'Jammu and Kashmir'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Maharashtra', 'Maharashtra'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('West Bengal', 'West Bengal'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli', 'Dadra and Nagar Haveli'), ('Daman and Diu', 'Daman and Diu'), ('Lakshadweep', 'Lakshadweep'), ('National Capital Territory of Delhi', 'National Capital Territory of Delhi'), ('Puducherry', 'Puducherry')], default='pending', max_length=50)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.customer')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveBigIntegerField(default=1)),
                ('Product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]