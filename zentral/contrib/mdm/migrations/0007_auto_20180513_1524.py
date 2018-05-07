# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-05-13 15:24
from __future__ import unicode_literals

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion
import zentral.contrib.mdm.models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0037_auto_20180213_1407'),
        ('mdm', '0006_enrolleduser'),
    ]

    operations = [
        migrations.CreateModel(
            name='DEPDevice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('serial_number', models.TextField(unique=True)),
                ('device_assigned_by', models.EmailField(editable=False, max_length=254)),
                ('device_assigned_date', models.DateTimeField(editable=False)),
                ('last_op_type', models.CharField(choices=[('added', 'Added'), ('modified', 'Modified'), ('deleted', 'Deleted')], editable=False, max_length=64, null=True)),
                ('last_op_date', models.DateTimeField(editable=False, null=True)),
                ('profile_status', models.CharField(choices=[('empty', 'Empty'), ('assigned', 'Assigned'), ('pushed', 'Pushed'), ('removed', 'Removed')], editable=False, max_length=64)),
                ('profile_uuid', models.UUIDField(editable=False, null=True, unique=True)),
                ('profile_assign_time', models.DateTimeField(editable=False, null=True)),
                ('profile_push_time', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DEPEnrollmentSession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('STARTED', 'Started'), ('SCEP_VERIFIED', 'SCEP verified'), ('AUTHENTICATED', 'Authenticated'), ('COMPLETED', 'Completed')], max_length=64)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            bases=(models.Model, zentral.contrib.mdm.models.EnrollmentSessionMixin),
        ),
        migrations.CreateModel(
            name='DEPOrganization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('identifier', models.CharField(max_length=128)),
                ('admin_id', models.EmailField(max_length=254)),
                ('name', models.TextField()),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.TextField()),
                ('address', models.TextField()),
                ('type', models.CharField(choices=[('edu', 'edu'), ('org', 'org')], max_length=3)),
                ('version', models.CharField(choices=[('v1', 'ADP'), ('v2', 'ASM')], max_length=2)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='DEPProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(editable=False, unique=True)),
                ('name', models.CharField(max_length=125, unique=True)),
                ('allow_pairing', models.BooleanField(default=False)),
                ('is_supervised', models.BooleanField(default=True)),
                ('is_multi_user', models.BooleanField(default=True)),
                ('is_mandatory', models.BooleanField(default=True)),
                ('await_device_configured', models.BooleanField(default=False)),
                ('auto_advance_setup', models.BooleanField(default=False)),
                ('is_mdm_removable', models.BooleanField(default=False)),
                ('skip_setup_items', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('AppleID', 'AppleID'), ('Biometric', 'Biometric'), ('Diagnostics', 'Diagnostics'), ('DisplayTone', 'DisplayTone'), ('Location', 'Location'), ('Passcode', 'Passcode'), ('Payment', 'Payment'), ('Privacy', 'Privacy'), ('Restore', 'Restore'), ('Siri', 'Siri'), ('TOS', 'TOS'), ('Zoom', 'Zoom'), ('Android', 'Android'), ('HomeButtonSensitivity', 'HomeButtonSensitivity'), ('OnBoarding', 'OnBoarding'), ('WatchMigration', 'WatchMigration'), ('FileVault', 'FileVault'), ('iCloudDiagnostics', 'iCloudDiagnostics'), ('iCloudStorage', 'iCloudStorage'), ('Registration', 'Registration'), ('ScreenSaver', 'ScreenSaver'), ('TapToSetup', 'TapToSetup'), ('TVHomeScreenSync', 'TVHomeScreenSync'), ('TVProviderSignIn', 'TVProviderSignIn'), ('TVRoom', 'TVRoom')], max_length=64), editable=False, size=None)),
                ('support_phone_number', models.CharField(blank=True, max_length=50)),
                ('support_email_address', models.EmailField(blank=True, max_length=250)),
                ('org_magic', models.CharField(blank=True, max_length=256)),
                ('department', models.CharField(blank=True, max_length=125)),
                ('include_tls_certificates', models.BooleanField(default=False)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('enrollment_secret', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, related_name='dep_profile', to='inventory.EnrollmentSecret')),
            ],
        ),
        migrations.CreateModel(
            name='DEPToken',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('certificate', models.BinaryField()),
                ('private_key', models.BinaryField()),
                ('consumer_key', models.CharField(editable=False, max_length=128, null=True)),
                ('consumer_secret', models.CharField(editable=False, max_length=128, null=True)),
                ('access_token', models.CharField(editable=False, max_length=128, null=True)),
                ('access_secret', models.CharField(editable=False, max_length=128, null=True)),
                ('access_token_expiry', models.DateTimeField(editable=False, null=True)),
                ('sync_cursor', models.CharField(editable=False, max_length=128, null=True)),
                ('last_synced_at', models.DateTimeField(editable=False, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='DEPVirtualServer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(editable=False)),
                ('uuid', models.UUIDField(editable=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('organization', models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mdm.DEPOrganization')),
                ('token', models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='virtual_server', to='mdm.DEPToken')),
            ],
        ),
        migrations.AddField(
            model_name='depprofile',
            name='virtual_server',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mdm.DEPVirtualServer'),
        ),
        migrations.AddField(
            model_name='depenrollmentsession',
            name='dep_profile',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mdm.DEPProfile'),
        ),
        migrations.AddField(
            model_name='depenrollmentsession',
            name='enrolled_device',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mdm.EnrolledDevice'),
        ),
        migrations.AddField(
            model_name='depenrollmentsession',
            name='enrollment_secret',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='dep_enrollment_session', to='inventory.EnrollmentSecret'),
        ),
        migrations.AddField(
            model_name='depenrollmentsession',
            name='scep_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='inventory.EnrollmentSecretRequest'),
        ),
        migrations.AddField(
            model_name='depdevice',
            name='profile',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='mdm.DEPProfile'),
        ),
        migrations.AddField(
            model_name='depdevice',
            name='virtual_server',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.CASCADE, to='mdm.DEPVirtualServer'),
        ),
    ]
