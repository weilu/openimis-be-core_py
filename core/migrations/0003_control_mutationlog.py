# Generated by Django 2.1.7 on 2019-08-21 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20190726_0701'),
    ]

    operations = [
        migrations.CreateModel(
            name='MutationLog',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('json_content', models.TextField()),
                ('request_date_time', models.DateTimeField(auto_now_add=True)),
                ('client_mutation_id', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.IntegerField()),
                ('error', models.TextField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING,
                                           to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'core_Mutation_Log',
                'managed': True,
            },
        ),
    ]
