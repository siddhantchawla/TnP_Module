# Generated by Django 2.0.3 on 2018-09-02 01:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_applicants'),
    ]

    operations = [
        migrations.AddField(
            model_name='applicants',
            name='comapny',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='company.Companies'),
        ),
    ]
