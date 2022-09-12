"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from library.views import AuthorModelViewSet, author_get, author_post
from users.views import CustomUserModelViewSet, CustomUserModelViewSet_limited
from TODO.views import ProjectModelViewSet, ToDoModelViewSet, ProjectModelViewSet_limited, ToDoModelViewSet_limited
from drf_yasg.views import get_schema_view
from drf_yasg.openapi import Info, License, Contact
from graphene_django.views import GraphQLView


schema_view = get_schema_view(
    Info(
        title='Library',
        default_version='1.0',
        description='some description',
        license=License(name='MIT'),
        contact=Contact(email='some@email.com')
    )

)


router = DefaultRouter()
router.register('authors', AuthorModelViewSet)
# router.register('CustomUser', CustomUserModelViewSet)
router.register('CustomUser', CustomUserModelViewSet_limited)
#router.register('Project', ProjectModelViewSet)
router.register('Project', ProjectModelViewSet_limited)
# router.register('ToDo', ToDoModelViewSet)
router.register('ToDo', ToDoModelViewSet_limited)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('api-auth-token/', views.obtain_auth_token),
    path('author_get/', author_get),
    path('author_get/<int:pk>', author_get),
    path('author_post/', author_post),
    path('author_post/<int:pk>', author_post),
    path('swagger', schema_view.with_ui()),
    path('graphql', GraphQLView.as_view(graphiql=True))
    # path('project/', )

]
