# Generated by Django 3.1.5 on 2021-02-27 05:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myaddresstable',
            name='agent_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.agenttable'),
        ),
        migrations.AlterField(
            model_name='myaddresstable',
            name='branch_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.branch'),
        ),
        migrations.AlterField(
            model_name='myaddresstable',
            name='partner_id',
            field=models.ForeignKey(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='agent.partner'),
        ),
    ]
