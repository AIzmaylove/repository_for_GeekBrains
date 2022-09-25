from rest_framework import mixins
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from .models import Project, ToDo
from .serializers import ProjectModelSerializer, ToDoModelSerializer
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from django_filters.rest_framework import DjangoFilterBackend
from .filters import TodoFilter


# class ProjectLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 10

class ProjectModelViewSet(ModelViewSet):

    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()

class ProjectModelViewSet_limited(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):

    # pagination_class = ProjectLimitOffsetPagination
    permission_classes = [DjangoModelPermissions]
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.all()



    def get_queryset(self):
        title = self.request.query_params.get('title', None)
        if title:
            return Project.objects.filter(title__contains=title)
        return Project.objects.all()

# class ToDoLimitOffsetPagination(LimitOffsetPagination):
#     default_limit = 20

class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()


class ToDoModelViewSet_limited(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    GenericViewSet
):
    # pagination_class = ToDoLimitOffsetPagination
    permission_classes = [DjangoModelPermissions]
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.all()
    filter_backends = [DjangoFilterBackend]
    filterset_class = TodoFilter


    def perform_destroy(self, instance):
        instance.closed = True
        instance.deleted = True
        instance.save()