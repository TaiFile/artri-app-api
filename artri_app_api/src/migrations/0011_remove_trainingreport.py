from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0010_remove_unused_report_fields"),
    ]

    operations = [
        migrations.DeleteModel(
            name="TrainingReport",
        ),
    ]
