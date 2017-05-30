# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-05-29 20:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ip', '0036_auto_20170526_1723'),
    ]

    operations = [
        migrations.RenameField(
            model_name='informationpackage',
            old_name='ArchivalInstitution',
            new_name='archival_institution',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='ArchivalLocation',
            new_name='archival_location',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='ArchivalType',
            new_name='archival_type',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='ArchivistOrganization',
            new_name='archivist_organization',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='Content',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='CreateDate',
            new_name='create_date',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='Enddate',
            new_name='end_date',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='Label',
            new_name='label',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='ObjectIdentifierValue',
            new_name='object_identifier_value',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='ObjectPath',
            new_name='object_path',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='Responsible',
            new_name='responsible',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='Startdate',
            new_name='start_date',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='State',
            new_name='state',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='SubmissionAgreement',
            new_name='submission_agreement',
        ),
        migrations.RenameField(
            model_name='informationpackage',
            old_name='SubmissionAgreementLocked',
            new_name='submission_agreement_locked',
        ),
    ]
