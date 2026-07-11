from src.models import (
    TrainingReport,
    DailyPainReport,
    DailySleepReport,
    DailySwellingReport,
    DailyFatigueReport,
)


class TrainingReportRepository:
    @staticmethod
    def list_for_user(user):
        return TrainingReport.objects.filter(user=user)


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
