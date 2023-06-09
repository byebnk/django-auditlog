# Generated by Django 4.2 on 2023-04-11 07:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import pgtrigger.compiler
import pgtrigger.migrations


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('action', models.CharField(choices=[('create', 'Create'), ('view', 'View'), ('update', 'Update'), ('delete', 'Delete'), ('login', 'Login'), ('logout', 'Logout'), ('login-failed', 'Login failed'), ('login-locked', 'Login locked'), ('admin-action', 'Admin action'), ('other', 'Other')], max_length=100)),
                ('description', models.CharField(blank=True, max_length=100, null=True)),
                ('object', models.CharField(max_length=100)),
                ('object_id', models.CharField(blank=True, max_length=100, null=True)),
                ('ip_address', models.GenericIPAddressField()),
                ('user_agent', models.CharField(blank=True, max_length=500, null=True)),
                ('principal', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        pgtrigger.migrations.AddTrigger(
            model_name='auditlog',
            trigger=pgtrigger.compiler.Trigger(name='read_only', sql=pgtrigger.compiler.UpsertTriggerSql(condition='WHEN (OLD.* IS DISTINCT FROM NEW.*)', func="RAISE EXCEPTION 'pgtrigger: Cannot update rows from % table', TG_TABLE_NAME;", hash='e9cd0e2ab7aeb4e220948a49e9f6180e833eb490', operation='UPDATE', pgid='pgtrigger_read_only_036ea', table='auditlog_auditlog', when='BEFORE')),
        ),
    ]
