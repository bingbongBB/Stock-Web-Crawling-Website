# Generated by Django 4.0.4 on 2022-06-16 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sampleApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StockHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.IntegerField(blank=True, null=True)),
                ('data', models.DateTimeField(blank=True, null=True)),
                ('capacity', models.IntegerField(blank=True, null=True)),
                ('turnover', models.IntegerField(blank=True, null=True)),
                ('open', models.FloatField(blank=True, null=True)),
                ('high', models.FloatField(blank=True, null=True)),
                ('low', models.FloatField(blank=True, null=True)),
                ('close', models.FloatField(blank=True, null=True)),
                ('change', models.FloatField(blank=True, null=True)),
                ('transaction', models.IntegerField(blank=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='s1301',
        ),
        migrations.DeleteModel(
            name='s1303',
        ),
        migrations.DeleteModel(
            name='s2317',
        ),
        migrations.DeleteModel(
            name='s2330',
        ),
        migrations.DeleteModel(
            name='s2412',
        ),
        migrations.DeleteModel(
            name='s2454',
        ),
        migrations.DeleteModel(
            name='s2603',
        ),
        migrations.DeleteModel(
            name='s2881',
        ),
        migrations.DeleteModel(
            name='s2882',
        ),
        migrations.DeleteModel(
            name='s6505',
        ),
    ]
