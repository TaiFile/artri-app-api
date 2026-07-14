from src.common.generics import UserScopedListCreateView, UserScopedRetrieveUpdateView

from .serializers import RemedySerializer
from .services import RemedyService


class RemedyListCreateView(UserScopedListCreateView):
    serializer_class = RemedySerializer
    service = RemedyService


class RemedyDetailView(UserScopedRetrieveUpdateView):
    serializer_class = RemedySerializer
    service = RemedyService
