from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Notes
from userapp.serializers import UserModelSerializer, BaseUserModelSerializer


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


class BaseProjectsModelSerializer(ModelSerializer):
    serializer_class = UserModelSerializer

    class Meta:
        model = Project
        fields = '__all__'

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return UserModelSerializer
        return BaseUserModelSerializer


class BaseNotesModelSerializer(ModelSerializer):
    serializer_class = ProjectsModelSerializer

    class Meta:
        model = Notes
        fields = '__all__'

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectsModelSerializer
        return BaseProjectsModelSerializer
