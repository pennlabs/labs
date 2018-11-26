# Generated by Django 2.0.8 on 2018-11-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('engagement', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='club',
            old_name='contact',
            new_name='email',
        ),
        migrations.AddField(
            model_name='club',
            name='facebook',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='club',
            name='founded',
            field=models.DateField(null=True),
        ),
    ]
