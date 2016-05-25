# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-24 16:47
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_store_owner', models.BooleanField(default=False)),
                ('school', models.CharField(max_length=40, null=True, verbose_name='대학이름')),
                ('major', models.CharField(help_text='본인이 속한 단과대학이나 동아리 이름을 적어주세요.', max_length=40, null=True, verbose_name='소속')),
                ('name', models.CharField(max_length=40, null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('phone', models.CharField(max_length=40, null=True)),
                ('favorites', models.ManyToManyField(blank=True, to='product.Product')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]