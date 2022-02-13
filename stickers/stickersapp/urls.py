"""stickersapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path, include, re_path

# from rest_framework.authtoken.views import obtain_auth_token
from graphene_django.views import GraphQLView
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from userapp.views import UserModelViewSet
from notesapp.views import ProjectModelViewSet, NoteModelViewSet, NotesLimitOffsetPaginatonViewSet, \
    NoteModelCreateViewAPISet
# from notesapp.views import NoteModelCreateViewAPISet
# from notesapp.views import ProjectModelViewAPISet, NoteModelListViewAPISet
# from notesapp.views import ProjectViewSet

from drf_yasg.views import get_schema_view
from drf_yasg import openapi

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', NoteModelViewSet)
router.register('pagination', NotesLimitOffsetPaginatonViewSet)
# router.register('v1-projects', ProjectViewSet, basename='project')
# router.register('list-projects', ProjectModelViewAPISet, basename='project')
# router.register('list-notes', NoteModelViewAPISet, basename='notes')

schema_view = get_schema_view(
    openapi.Info(
        title="Library",
        default_version='0.1.0',
        description="Documentation to test REST API project",
        contact=openapi.Contact(email="agentstorm@ya.ru"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)

urlpatterns = [
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
    path('admin/', admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    # path('api-token-auth/', obtain_auth_token),
    path('api/', include(router.urls)),
    path('api/v<int:version>/projects', ProjectModelViewSet.as_view({'get': 'list'}), name='projects_api'),
    path('api/v<int:version>/notes', NoteModelViewSet.as_view({'get': 'list'}), name='notes_api'),
    # path('v2/projects', ProjectModelViewAPISet.as_view()),
    # path('v2/notes/list', NoteModelListViewAPISet.as_view()),
    path('v2/notes/add', NoteModelCreateViewAPISet.as_view()),
    path("graphql/", GraphQLView.as_view(graphiql=True)),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
