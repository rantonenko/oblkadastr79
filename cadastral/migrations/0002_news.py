# Generated by Django 2.2.12 on 2021-03-07 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastral', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('text', models.TextField()),
                ('pub_date', models.DateTimeField(auto_now_add=True, db_index=True, verbose_name='Дата публикации')),
                ('image', models.ImageField(blank=True, null=True, upload_to='news/')),
            ],
        ),
    ]
