from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Notes
from userapp.serializers import UserModelSerializer


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'repo_link', 'included_users')


class NotesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        exclude = ['updated_at']


class ProjectsModelAPISerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'repo_link', 'included_users')


class NotesModelAPISerializer(ModelSerializer):
    class Meta:
        model = Notes
        exclude = ['updated_at']
