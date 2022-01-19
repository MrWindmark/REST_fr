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
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from userapp.views import UserModelViewSet
from notesapp.views import ProjectModelViewSet, NoteModelViewSet, NoteModelCreateViewAPISet
from notesapp.views import ProjectModelViewAPISet, NoteModelListViewAPISet
from notesapp.views import ProjectViewSet

router = DefaultRouter()
router.register('users', UserModelViewSet)
router.register('projects', ProjectModelViewSet)
router.register('notes', NoteModelViewSet)
# router.register('v1-projects', ProjectViewSet, basename='project')
# router.register('list-projects', ProjectModelViewAPISet, basename='project')
# router.register('list-notes', NoteModelViewAPISet, basename='notes')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('v2/projects', ProjectModelViewAPISet.as_view()),
    path('v2/notes/list', NoteModelListViewAPISet.as_view()),
    path('v2/notes/add', NoteModelCreateViewAPISet.as_view()),
]
