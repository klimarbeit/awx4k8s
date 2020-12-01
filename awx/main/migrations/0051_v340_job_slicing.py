# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-10-15 16:21
from __future__ import unicode_literals

import awx.main.utils.polymorphic
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0050_v340_drop_celery_tables'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='job_slice_count',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='If ran as part of sliced jobs, the total number of slices. If 1, job is not part of a sliced job.'),
        ),
        migrations.AddField(
            model_name='job',
            name='job_slice_number',
            field=models.PositiveIntegerField(blank=True, default=0, help_text='If part of a sliced job, the ID of the inventory slice operated on. If not part of sliced job, parameter is not used.'),
        ),
        migrations.AddField(
            model_name='jobtemplate',
            name='job_slice_count',
            field=models.PositiveIntegerField(blank=True, default=1, help_text='The number of jobs to slice into at runtime. Will cause the Job Template to launch a workflow if value is greater than 1.'),
        ),
        migrations.AddField(
            model_name='workflowjob',
            name='is_sliced_job',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='workflowjob',
            name='job_template',
            field=models.ForeignKey(blank=True, default=None, help_text='If automatically created for a sliced job run, the job template the workflow job was created from.', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='slice_workflow_jobs', to='main.JobTemplate'),
        ),
        migrations.AlterField(
            model_name='unifiedjob',
            name='unified_job_template',
            field=models.ForeignKey(default=None, editable=False, null=True, on_delete=awx.main.utils.polymorphic.SET_NULL, related_name='unifiedjob_unified_jobs', to='main.UnifiedJobTemplate'),
        ),
    ]
