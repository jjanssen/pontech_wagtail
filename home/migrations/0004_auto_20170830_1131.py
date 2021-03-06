# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-30 11:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailcore', '0040_page_draft_title'),
        ('wagtailimages', '0019_delete_filter'),
        ('wagtailtrans', '0006_auto_20161212_2020'),
        ('home', '0003_auto_20170830_1043'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPostsPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='wagtailcore.Page')),
                ('translatablepage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage')),
                ('header_text', models.CharField(max_length=255)),
                ('header_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.Image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailtrans.translatablepage', 'wagtailcore.page'),
        ),
        migrations.RemoveField(
            model_name='blogpost',
            name='id',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='page_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='wagtailcore.Page'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='translatablepage_ptr',
            field=models.OneToOneField(auto_created=True, default='', on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailtrans.TranslatablePage'),
            preserve_default=False,
        ),
    ]
