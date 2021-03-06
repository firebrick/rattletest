# Generated by Django 4.0.3 on 2022-03-06 05:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("projects", "0004_rename_created_at_module_created_date_and_more"),
        ("testcases", "0004_alter_testcase_created_by"),
    ]

    operations = [
        migrations.AddField(
            model_name="testcase",
            name="module",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.CASCADE,
                to="projects.module",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="testcase",
            name="created_by",
            field=models.ForeignKey(
                on_delete=models.SET(-99),
                related_name="tc_created_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="testcase",
            name="modified_by",
            field=models.ForeignKey(
                on_delete=models.SET(-99),
                related_name="tc_modified_by",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
