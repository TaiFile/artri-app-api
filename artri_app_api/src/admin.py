from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Remedy, TrainingReport, DailyPainReport, Exercise, Training, DailySleepReport, DailySwellingReport, DailyFatigueReport

# Configuração para o model User (customizado)
class CustomUserAdmin(UserAdmin):
    # Campos a serem exibidos na lista de usuários no Admin
    list_display = ("username", "email", "first_name", "last_name", "birth_date", "weight", "height")
    
    # Campos adicionais para edição no Admin (incluindo os campos personalizados)
    fieldsets = UserAdmin.fieldsets + (
        ("Informações Pessoais", {"fields": ("birth_date", "weight", "height")}),
    )

# Configuração para o model remedy
class RemedyAdmin(admin.ModelAdmin):
    # Campos exibidos na lista de remédios
    list_display = ("name", "user", "hour", "quantity")

    # Filtros laterais
    list_filter = ("user",)
    
    # Campos de busca
    search_fields = ("name", "description")

class ExerciseAdmin(admin.ModelAdmin):
    list_display = ("name", "difficulty")

    list_filter = ("difficulty",)

    search_fields = ("name", "description")

class TrainingAdmin(admin.ModelAdmin):
    list_display = ("name", "difficulty")

    list_filter = ("difficulty",)

    search_fields = ("name", "description")

class DailySleepReportAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "sleep_duration", "sleep_quality")

    list_filter = ("user", "date", "sleep_quality")

    search_fields = ("user__username",)

class DailySwellingReportAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "swelling_level", "swelling_location")

    list_filter = ("user", "date", "swelling_level")

    search_fields = ("user__username", "swelling_location")

class DailyFatigueReportAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "fatigue_level")

    list_filter = ("user", "date", "fatigue_level")
    
    search_fields = ("user__username", "fatigue_description")

class TrainingReportAdmin(admin.ModelAdmin):
    list_display = ("user", "training", "date")
    
    list_filter = ("user", "training", "date")
    
    search_fields = ("user__username", "training__name")

class DailyPainReportAdmin(admin.ModelAdmin):
    list_display = ("user", "date", "pain_level", "pain_location")
    
    list_filter = ("user", "date", "pain_level")
    
    search_fields = ("user__username", "pain_location")

admin.site.register(User, CustomUserAdmin)
admin.site.register(Remedy, RemedyAdmin)
admin.site.register(TrainingReport, TrainingReportAdmin)
admin.site.register(DailyPainReport, DailyPainReportAdmin)
admin.site.register(Exercise, ExerciseAdmin)
admin.site.register(Training, TrainingAdmin)
admin.site.register(DailySleepReport, DailySleepReportAdmin)
admin.site.register(DailySwellingReport, DailySwellingReportAdmin)
admin.site.register(DailyFatigueReport, DailyFatigueReportAdmin)