# Generated by Django 5.0.6 on 2024-06-28 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AvatarImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='avatars/')),
            ],
        ),
        migrations.AddField(
            model_name='contactinfo',
            name='telegram',
            field=models.URLField(default='qfqefwef'),
            preserve_default=False,
        ),
    ]
