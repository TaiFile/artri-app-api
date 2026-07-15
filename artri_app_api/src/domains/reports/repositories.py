from src.models import (
    DailyPainReport,
    DailySleepReport,
    DailySwellingReport,
    DailyFatigueReport,
)


class DailyPainReportRepository:
    @staticmethod
    def list_for_user(user):
        return DailyPainReport.objects.filter(user=user)


class DailySleepReportRepository:
    @staticmethod
    def list_for_user(user):
        return DailySleepReport.objects.filter(user=user)


class DailySwellingReportRepository:
    @staticmethod
    def list_for_user(user):
        return DailySwellingReport.objects.filter(user=user)


class DailyFatigueReportRepository:
    @staticmethod
    def list_for_user(user):
        return DailyFatigueReport.objects.filter(user=user)
