from .repositories import (
    DailyPainReportRepository,
    DailySleepReportRepository,
    DailySwellingReportRepository,
    DailyFatigueReportRepository,
)


class DailyPainReportService:
    @staticmethod
    def list_for_user(user):
        return DailyPainReportRepository.list_for_user(user)


class DailySleepReportService:
    @staticmethod
    def list_for_user(user):
        return DailySleepReportRepository.list_for_user(user)


class DailySwellingReportService:
    @staticmethod
    def list_for_user(user):
        return DailySwellingReportRepository.list_for_user(user)


class DailyFatigueReportService:
    @staticmethod
    def list_for_user(user):
        return DailyFatigueReportRepository.list_for_user(user)
