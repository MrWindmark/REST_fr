from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Project, Notes
from userapp.serializers import UserModelSerializer, BaseUserModelSerializer


# v1
class ProjectsModelAPISerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = ('name', 'repo_link')


# v1
class BaseProjectsModelSerializer(ModelSerializer):
    serializer_class = UserModelSerializer
    included_users = BaseUserModelSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'repo_link', 'included_users')

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return BaseUserModelSerializer
        return UserModelSerializer


# v1.3
class ProjectsModelSerializer(HyperlinkedModelSerializer):
    included_users = UserModelSerializer(many=True, read_only=True)

    class Meta:
        model = Project
        fields = ('name', 'repo_link', 'included_users')


# v1
class NotesModelAPISerializer(ModelSerializer):
    class Meta:
        model = Notes
        exclude = ['updated_at']


# v2
class BaseNotesModelSerializer(ModelSerializer):
    serializer_class = BaseProjectsModelSerializer
    project_id = ProjectsModelSerializer(read_only=True)

    class Meta:
        model = Notes
        fields = ('title', 'inner_text', 'created_at', 'Date', 'is_complited', 'project_id')

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return ProjectsModelSerializer
        return BaseProjectsModelSerializer


# v1.3
class NotesModelSerializer(HyperlinkedModelSerializer):
    project_id = ProjectsModelSerializer(read_only=True)
    creator = UserModelSerializer(read_only=True)

    class Meta:
        model = Notes
        fields = ('title', 'inner_text', 'Date', 'creator', 'project_id')
        # exclude = ['updated_at']
