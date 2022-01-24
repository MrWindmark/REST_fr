from rest_framework.viewsets import ModelViewSet

# Create your views here.
from notesapp.models import Project, Notes
from notesapp.serializers import ProjectsModelSerializer, NotesModelSerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsModelSerializer


class NoteModelViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer
