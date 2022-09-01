from rest_framework import mixins
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import CustomUser
from .serializers import CustomUserModelSerializer
from rest_framework.decorators import action


class CustomUserModelViewSet(ModelViewSet):
    serializer_class = CustomUserModelSerializer
    queryset = CustomUser.objects.all()


class CustomUserModelViewSet_limited(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet
):

    serializer_class = CustomUserModelSerializer
    queryset = CustomUser.objects.all()

    @action(detail=True, methods=['get'])
    def get_CustomUser_name(self, request, pk):
        customUser = get_object_or_404(CustomUser, pk=pk)
        return Response({'first_name': str(customUser.first_name)})