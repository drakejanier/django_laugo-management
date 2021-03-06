# Generated by Django 2.2.1 on 2019-05-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itmName', models.CharField(max_length=100)),
                ('itmType', models.CharField(choices=[('MEDICINE', 'MEDICINE'), ('FOOD', 'FOOD'), ('OTHERS', 'OTHERS')], default='MEDICINE', max_length=20)),
                ('itmQty', models.IntegerField(default=0)),
                ('itmUnit', models.CharField(default='unit(s)', max_length=10)),
                ('itmStatus', models.CharField(choices=[('AVAILABLE', 'AVAILABLE'), ('UNAVAILABLE', 'OUT OF STOCK'), ('RESTOCKING', 'RESTOCKING')], default='AVAILABLE', max_length=20)),
                ('supplierID', models.IntegerField(default=0)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
