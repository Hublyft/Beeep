# Generated by Django 3.0.2 on 2020-11-26 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_lawyer_on_call'),
    ]

    operations = [
        migrations.AddField(
            model_name='lawyer',
            name='scn_number',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]