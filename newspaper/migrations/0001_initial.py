# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime
import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classifield',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('price', models.FloatField(default=0, verbose_name='Price')),
                ('image', models.ImageField(default=None, upload_to=b'documents/imagen/classifield/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': 'Classifield',
                'verbose_name_plural': 'Classifields',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('text', models.TextField(verbose_name='Text')),
                ('image', models.ImageField(default=None, upload_to=b'documents/imagen/comment/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
                ('dating_comment', models.DateTimeField(default=datetime.datetime.now, verbose_name='Dating Comment')),
            ],
            options={
                'ordering': ['-dating_comment'],
                'verbose_name': 'Comment',
                'verbose_name_plural': 'Comments',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Creation',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('creation', models.DateTimeField(default=datetime.datetime.now, null=True, verbose_name='Creation', blank=True)),
            ],
            options={
                'ordering': ['-creation'],
                'verbose_name': 'Creation',
                'verbose_name_plural': 'Creations',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=500, verbose_name='Title')),
                ('subtitle', models.TextField(verbose_name='Subtitle')),
                ('description', models.TextField(verbose_name='Description')),
                ('dating_news', models.DateTimeField(default=datetime.datetime.now, verbose_name='Dating News')),
                ('image', models.ImageField(default=None, upload_to=b'documents/imagen/news/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
            ],
            options={
                'ordering': ['-dating_news'],
                'verbose_name': 'News',
                'verbose_name_plural': 'News',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date_offer', models.DateTimeField(null=True, verbose_name='Dating Offer', blank=True)),
                ('value', models.FloatField(default=0, verbose_name='Value')),
                ('phone', models.CharField(max_length=15, verbose_name='Phone')),
            ],
            options={
                'ordering': ['-value'],
                'verbose_name': 'Offer',
                'verbose_name_plural': 'Offers',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('image', models.ImageField(default=None, upload_to=b'documents/imagen/page/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': 'Section',
                'verbose_name_plural': 'Sections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='SubSection',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('description', models.TextField(verbose_name='Description')),
                ('image', models.ImageField(default=None, upload_to=b'documents/imagen/page/%Y/%m/%d', null=True, verbose_name='Image', blank=True)),
                ('sections', models.ManyToManyField(to='newspaper.Section', verbose_name='Sections')),
            ],
            options={
                'ordering': ['-title'],
                'verbose_name': 'SubSection',
                'verbose_name_plural': 'SubSections',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
                'verbose_name': 'User',
                'verbose_name_plural': 'Users',
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Anonymous',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='newspaper.User')),
            ],
            options={
                'verbose_name': 'Anonymous',
                'verbose_name_plural': 'Anonymous',
            },
            bases=('newspaper.user',),
        ),
        migrations.CreateModel(
            name='UserAutheticated',
            fields=[
                ('user_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='newspaper.User')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(default=django.utils.timezone.now, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Required. 30 characters or fewer. Letters, digits and @/./+/-/_ only.', unique=True, max_length=30, verbose_name='username', validators=[django.core.validators.RegexValidator('^[\\w.@+-]+$', 'Enter a valid username.', 'invalid')])),
                ('first_name', models.CharField(max_length=30, verbose_name='first name', blank=True)),
                ('last_name', models.CharField(max_length=30, verbose_name='last name', blank=True)),
                ('email', models.EmailField(max_length=75, verbose_name='email address', blank=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('profile_image', models.ImageField(default=None, upload_to=b'documents/imagen/profile_image/%Y/%m/%d', null=True, verbose_name='Profile Image', blank=True)),
            ],
            options={
                'ordering': ['-first_name'],
                'db_table': 'auth_user',
                'verbose_name': 'User Autheticated',
                'verbose_name_plural': 'Users Autheticated',
            },
            bases=('newspaper.user', models.Model),
        ),
        migrations.CreateModel(
            name='Redator',
            fields=[
                ('userautheticated_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Redator',
                'verbose_name_plural': 'Redators',
            },
            bases=('newspaper.userautheticated',),
        ),
        migrations.CreateModel(
            name='Lector',
            fields=[
                ('userautheticated_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Lector',
                'verbose_name_plural': 'Lectors',
            },
            bases=('newspaper.userautheticated',),
        ),
        migrations.CreateModel(
            name='Journalist',
            fields=[
                ('userautheticated_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Journalist',
                'verbose_name_plural': 'Journalists',
            },
            bases=('newspaper.userautheticated',),
        ),
        migrations.AddField(
            model_name='offer',
            name='author_offer',
            field=models.ForeignKey(verbose_name='Author', to='newspaper.Lector'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='author',
            field=models.ForeignKey(verbose_name='Author', to='newspaper.Journalist'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='comments',
            field=models.ManyToManyField(to='newspaper.Comment', null=True, verbose_name='Comments', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='news',
            name='subsection',
            field=models.ForeignKey(verbose_name='SubSection', to='newspaper.SubSection'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(verbose_name='Author', to='newspaper.Lector'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classifield',
            name='creator_classifield',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, verbose_name='Creador Classifield', blank=True, to='newspaper.Lector', null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='classifield',
            name='offers',
            field=models.ManyToManyField(to='newspaper.Offer', null=True, verbose_name='Offers', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userautheticated',
            name='groups',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Group', blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of his/her group.', verbose_name='groups'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='userautheticated',
            name='user_permissions',
            field=models.ManyToManyField(related_query_name='user', related_name='user_set', to='auth.Permission', blank=True, help_text='Specific permissions for this user.', verbose_name='user permissions'),
            preserve_default=True,
        ),
    ]
