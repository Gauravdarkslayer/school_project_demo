# Generated by Django 3.1.2 on 2020-11-13 16:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('test_gen', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='organization_test_create',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('logo', models.ImageField(upload_to='media/')),
                ('test_name', models.CharField(max_length=100)),
                ('college_name', models.CharField(blank=True, max_length=100, null=True)),
                ('cam_micro', models.CharField(choices=[('yes', 'yes'), ('no', 'no')], max_length=3)),
                ('test_duration', models.CharField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='user_questionnaire',
            name='user_id',
        ),
        migrations.DeleteModel(
            name='question_options',
        ),
        migrations.DeleteModel(
            name='user_questionnaire',
        ),
    ]
