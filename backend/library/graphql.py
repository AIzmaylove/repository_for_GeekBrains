import graphene
from graphene_django import DjangoObjectType
from .models import Author
from users.models import CustomUser
from TODO.models import ToDo, Project

class CustomUserObjectType(DjangoObjectType):
    class Meta:
        model = CustomUser
        fields = '__all__'


class ToDoObjectType(DjangoObjectType):
    class Meta:
        model = ToDo
        fields = '__all__'

class ProjectObjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = '__all__'


class AuthorObjectType(DjangoObjectType):
    class Meta:
        model = Author
        fields = '__all__'



class Query(graphene.ObjectType):

    all_authors = graphene.List(AuthorObjectType)

    def resolve_all_authors(self, info):
        return Author.objects.all()

    all_customusers = graphene.List(CustomUserObjectType)

    def resolve_all_customusers(self, info):
        return CustomUser.objects.all()

    all_todo = graphene.List(ToDoObjectType)

    def resolve_all_todo(self, info):
        return ToDo.objects.all()

    all_projects = graphene.List(ProjectObjectType)

    def resolve_all_projects(self, info):
        return Project.objects.all()

    get_author_by_id = graphene.Field(AuthorObjectType, pk=graphene.Int(required=True))
    def resolve_get_author_by_id(self, info, pk):
        return Author.objects.get(pk=pk)

    todo_by_project_title = graphene.List(ToDoObjectType, title=graphene.String(required=False))
    def resolve_todo_by_project_title(self, info, title=None):
        todos = ToDo.objects.all()
        if title:
            todos = todos.filter(project__title=title)
        return todos



schema = graphene.Schema(query=Query)