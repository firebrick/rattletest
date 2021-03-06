# Generated by Django 4.0.3 on 2022-03-02 01:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("testcases", "0002_alter_testcase_title"),
    ]

    operations = [
        migrations.AddField(
            model_name="testcase",
            name="modified_by",
            field=models.ForeignKey(
                default=1,
                on_delete=django.db.models.deletion.RESTRICT,
                related_name="tc_modified_by",
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
