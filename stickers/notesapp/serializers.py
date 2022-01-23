from rest_framework import serializers
from rest_framework.relations import StringRelatedField
from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Notes
from userapp.serializers import UserModelSerializer


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    included_users = UserModelSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'repo_link', 'included_users')


class NotesModelSerializer(HyperlinkedModelSerializer):
    project_id = ProjectsModelSerializer(read_only=True)
    creator = UserModelSerializer(read_only=True)

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
