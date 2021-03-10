# Generated by Django 2.2.17 on 2021-01-12 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Act',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=20)),
                ('pub_date', models.DateField()),
                ('num_obj', models.PositiveIntegerField()),
                ('type_act', models.CharField(choices=[('act', 'Акт'), ('report', 'Отчёт')], max_length=6)),
                ('path', models.FileField(upload_to='files/acts/')),
            ],
        ),
    ]
