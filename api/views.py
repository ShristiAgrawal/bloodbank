from rest_framework import viewsets

from .serializers import ASerializer
from .models import A


class AViewSet(viewsets.ModelViewSet):
    queryset = A.objects.all().order_by('name')
    serializer_class = ASerializer