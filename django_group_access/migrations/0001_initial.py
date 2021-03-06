# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-14 10:05


from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AccessGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True)),
                ('supergroup', models.BooleanField(default=False)),
                ('can_be_shared_with', models.BooleanField(default=True)),
                ('auto_share_groups', models.ManyToManyField(blank=True, related_name='_accessgroup_auto_share_groups_+', to='django_group_access.AccessGroup')),
                ('can_share_with', models.ManyToManyField(blank=True, to='django_group_access.AccessGroup')),
                ('members', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
    ]
