# Generated by Django 2.1.3 on 2018-11-19 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20181119_1328'),
    ]

    operations = [
        migrations.AlterField(
            model_name='asset',
            name='currentLocation',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Location'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='employee',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Employee'),
        ),
        migrations.AlterField(
            model_name='asset',
            name='manufacturer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Manufacturer'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='location',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.Location'),
        ),
    ]