# Generated by Django 4.1.1 on 2022-10-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=122)),
                ('lname', models.CharField(max_length=122)),
                ('fname', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('pass1', models.CharField(max_length=122)),
                ('pass2', models.CharField(max_length=122)),
                ('date', models.DateField()),
            ],
        ),
    ]
