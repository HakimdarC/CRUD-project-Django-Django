# Generated by Django 2.1.3 on 2019-04-30 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='webpage',
            options={'ordering': ['-name']},
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='webpage', to='myapp.Topic'),
        ),
    ]
