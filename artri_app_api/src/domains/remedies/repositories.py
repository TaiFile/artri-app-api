from src.models import Remedy


class RemedyRepository:
    @staticmethod
    def list_for_user(user):
        return Remedy.objects.filter(user=user, quantity__gt=0)

    @staticmethod
    def detail_queryset_for_user(user):
        return Remedy.objects.filter(user=user)
