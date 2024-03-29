# Generated by Django 3.2.16 on 2023-12-10 08:03

import account_handler.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to=account_handler.models.user_profile_picture)),
                ('description', models.TextField(blank=True, null=True)),
                ('roll_number', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('is_alumni', models.BooleanField(default=False)),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricalUserProfile',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('profile_picture', models.TextField(blank=True, max_length=100, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('roll_number', models.CharField(blank=True, max_length=64, null=True)),
                ('type', models.CharField(blank=True, max_length=32, null=True)),
                ('mobile', models.CharField(blank=True, max_length=255, null=True)),
                ('is_alumni', models.BooleanField(default=False)),
                ('sex', models.CharField(blank=True, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')], max_length=10, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical user profile',
                'verbose_name_plural': 'historical user profiles',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
    ]
