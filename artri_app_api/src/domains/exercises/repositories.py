from src.models import Exercise


class ExerciseRepository:
    @staticmethod
    def all():
        return Exercise.objects.all()

    @staticmethod
    def with_category():
        return Exercise.objects.exclude(category__isnull=True).exclude(category='')

    @staticmethod
    def filter_by_category(queryset, category):
        return queryset.filter(category=category)

    @staticmethod
    def filter_by_difficulty(queryset, difficulty):
        # O app envia 'easy'/'medium'/'hard'; o banco guarda 'Easy'/'Medium'/'Hard'.
        return queryset.filter(difficulty__iexact=difficulty)
