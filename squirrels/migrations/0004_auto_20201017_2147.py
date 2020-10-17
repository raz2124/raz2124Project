# Generated by Django 3.1.2 on 2020-10-17 21:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('squirrels', '0003_squirrel_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='squirrel',
            name='name',
        ),
        migrations.AddField(
            model_name='squirrel',
            name='unique_id',
            field=models.CharField(help_text='Unique Identifier for Squirrel', max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='squirrel',
            name='date',
            field=models.DateTimeField(auto_now_add=True, help_text='Day the Squirrel was Sighted'),
        ),
    ]