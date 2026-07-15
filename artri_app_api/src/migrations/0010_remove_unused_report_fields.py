from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0009_remove_remedy_days_of_week"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="dailyfatiguereport",
            name="fatigue_description",
        ),
        migrations.RemoveField(
            model_name="dailysleepreport",
            name="sleep_duration",
        ),
        migrations.RemoveField(
            model_name="dailysleepreport",
            name="sleep_quality",
        ),
    ]
