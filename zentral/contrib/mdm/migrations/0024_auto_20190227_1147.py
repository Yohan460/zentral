# Generated by Django 2.1.7 on 2019-02-27 11:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mdm', '0023_auto_20180927_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='configurationprofile',
            name='meta_business_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.MetaBusinessUnit'),
        ),
        migrations.AlterField(
            model_name='depenrollmentsession',
            name='enrollment_secret',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='dep_enrollment_session', to='inventory.EnrollmentSecret'),
        ),
        migrations.AlterField(
            model_name='depenrollmentsession',
            name='scep_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='inventory.EnrollmentSecretRequest'),
        ),
        migrations.AlterField(
            model_name='depprofile',
            name='enrollment_secret',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='dep_profile', to='inventory.EnrollmentSecret'),
        ),
        migrations.AlterField(
            model_name='depvirtualserver',
            name='organization',
            field=models.ForeignKey(editable=False, on_delete=django.db.models.deletion.PROTECT, to='mdm.DEPOrganization'),
        ),
        migrations.AlterField(
            model_name='depvirtualserver',
            name='token',
            field=models.OneToOneField(editable=False, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='virtual_server', to='mdm.DEPToken'),
        ),
        migrations.AlterField(
            model_name='kernelextension',
            name='team',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mdm.KernelExtensionTeam'),
        ),
        migrations.AlterField(
            model_name='kernelextensionpolicy',
            name='meta_business_unit',
            field=models.OneToOneField(editable=False, on_delete=django.db.models.deletion.PROTECT, related_name='kernel_extension_policy', to='inventory.MetaBusinessUnit'),
        ),
        migrations.AlterField(
            model_name='mdmenrollmentpackage',
            name='meta_business_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='inventory.MetaBusinessUnit'),
        ),
        migrations.AlterField(
            model_name='otaenrollment',
            name='enrollment_secret',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='ota_enrollment', to='inventory.EnrollmentSecret'),
        ),
        migrations.AlterField(
            model_name='otaenrollmentsession',
            name='enrollment_secret',
            field=models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='ota_enrollment_session', to='inventory.EnrollmentSecret'),
        ),
        migrations.AlterField(
            model_name='otaenrollmentsession',
            name='phase2_scep_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='inventory.EnrollmentSecretRequest'),
        ),
        migrations.AlterField(
            model_name='otaenrollmentsession',
            name='phase3_scep_request',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='inventory.EnrollmentSecretRequest'),
        ),
    ]
