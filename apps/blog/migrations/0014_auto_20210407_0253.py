# Generated by Django 3.1.7 on 2021-04-07 02:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0013_categorypostdesa_postdesa'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postdesa',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='postDesas', to='blog.categorypostdesa'),
        ),
    ]