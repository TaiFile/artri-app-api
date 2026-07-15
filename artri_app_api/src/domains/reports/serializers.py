from rest_framework import serializers

from src.models import (
    DailyPainReport,
    DailySleepReport,
    DailySwellingReport,
    DailyFatigueReport,
)


class DailyPainReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyPainReport
        fields = '__all__'
        read_only_fields = ('user', 'created_at')


class DailySleepReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySleepReport
        fields = '__all__'
        read_only_fields = ('user', 'created_at')


class DailySwellingReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailySwellingReport
        fields = '__all__'
        read_only_fields = ('user', 'created_at')


class DailyFatigueReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyFatigueReport
        fields = '__all__'
        read_only_fields = ('user', 'created_at')
