from .repositories import RemedyRepository


class RemedyService:
    @staticmethod
    def list_for_user(user):
        return RemedyRepository.list_for_user(user)

    @staticmethod
    def detail_queryset_for_user(user):
        return RemedyRepository.detail_queryset_for_user(user)
