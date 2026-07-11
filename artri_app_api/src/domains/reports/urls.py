from django.urls import path

from .controllers import (
    TrainingReportListCreateView,
    DailyPainReportListCreateView,
    DailySleepReportListCreateView,
    DailySwellingReportListCreateView,
    DailyFatigueReportListCreateView,
)

urlpatterns = [
    path('training-reports/', TrainingReportListCreateView.as_view(), name='training-report-list-create'),
    path('daily-pain-reports/', DailyPainReportListCreateView.as_view(), name='daily-pain-report-list-create'),
    path('daily-sleep-reports/', DailySleepReportListCreateView.as_view(), name='daily-sleep-report-list-create'),
    path('daily-swelling-reports/', DailySwellingReportListCreateView.as_view(), name='daily-swelling-report-list-create'),
    path('daily-fatigue-reports/', DailyFatigueReportListCreateView.as_view(), name='daily-fatigue-report-list-create'),
]
