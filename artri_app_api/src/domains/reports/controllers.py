from src.common.generics import UserScopedListCreateView

from .serializers import (
    DailyPainReportSerializer,
    DailySleepReportSerializer,
    DailySwellingReportSerializer,
    DailyFatigueReportSerializer,
)
from .services import (
    DailyPainReportService,
    DailySleepReportService,
    DailySwellingReportService,
    DailyFatigueReportService,
)


class DailyPainReportListCreateView(UserScopedListCreateView):
    serializer_class = DailyPainReportSerializer
    service = DailyPainReportService


class DailySleepReportListCreateView(UserScopedListCreateView):
    serializer_class = DailySleepReportSerializer
    service = DailySleepReportService


class DailySwellingReportListCreateView(UserScopedListCreateView):
    serializer_class = DailySwellingReportSerializer
    service = DailySwellingReportService


class DailyFatigueReportListCreateView(UserScopedListCreateView):
    serializer_class = DailyFatigueReportSerializer
    service = DailyFatigueReportService
