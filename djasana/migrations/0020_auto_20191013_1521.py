# Generated by Django 2.2.5 on 2019-10-13 15:21

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('djasana', '0019_adds_project_is_template'),
    ]

    operations = [
        migrations.AddField(
            model_name='projectstatus',
            name='author',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='status_owner', to='djasana.User', to_field='remote_id'),
        ),
        migrations.AddField(
            model_name='projectstatus',
            name='modified_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='download_url',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='permanent_url',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='attachment',
            name='view_url',
            field=models.TextField(validators=[django.core.validators.URLValidator()]),
        ),
        migrations.AlterField(
            model_name='project',
            name='owner',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='projects_owner', to='djasana.User', to_field='remote_id'),
        ),
    ]
