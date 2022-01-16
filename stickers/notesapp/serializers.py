from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Project, Notes


class ProjectsModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'repo_link', 'included_users')


class NotesModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Notes
        fields = '__all__'
