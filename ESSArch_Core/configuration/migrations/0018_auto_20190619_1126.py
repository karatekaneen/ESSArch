# Generated by Django 2.2.2 on 2019-06-19 09:26

from django.db import migrations, models
import django.db.models.deletion

from ESSArch_Core.storage.models import DISK, StorageMethod


def set_storage_method(apps, schema_editor):
    StoragePolicy = apps.get_model("configuration", "StoragePolicy")

    for policy in StoragePolicy.objects.all():
        fastest_method = StorageMethod.objects.fastest().filter(
            storage_policies__id=policy.pk, type=DISK
        ).first()

        if fastest_method is None:
            raise ValueError('No storage method available for cache')

        policy.cache_storage_id = fastest_method.pk
        policy.save()


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0017_auto_20190619_1041'),
        ('storage', '0036_auto_20190619_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='storagepolicy',
            name='cache_storage',
            field=models.ForeignKey(db_constraint=False, on_delete=django.db.models.deletion.PROTECT, related_name='cache_policy', to='storage.StorageMethod'),
        ),
        migrations.RunPython(set_storage_method, migrations.RunPython.noop),
        migrations.AlterField(
            model_name='storagepolicy',
            name='cache_storage',
            field=models.ForeignKey(db_constraint=True, on_delete=django.db.models.deletion.PROTECT, related_name='cache_policy', to='storage.StorageMethod'),
        ),
    ]
