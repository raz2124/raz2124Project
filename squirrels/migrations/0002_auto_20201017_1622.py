# Generated by Django 3.0.7 on 2020-10-17 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='squirrel',
            name='age',
            field=models.CharField(choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?')], default='AM', help_text='How old was this squirrel', max_length=20),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='latitude',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='longitude',
            field=models.DecimalField(decimal_places=2, max_digits=5, null=True),
        ),
        migrations.AddField(
            model_name='squirrel',
            name='shift',
            field=models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], default='AM', help_text='Time of Day', max_length=20),
        ),
    ]