from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView

# Create your views here.
from notesapp.models import Project, Notes
from notesapp.serializers import ProjectsModelSerializer, NotesModelSerializer
from notesapp.serializers import ProjectsModelAPISerializer, NotesModelAPISerializer


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsModelSerializer


class NoteModelViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer


class ProjectModelViewAPISet(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectsModelAPISerializer(projects, many=True)
        return Response(serializer.data)


class NoteModelViewAPISet(APIView):
    renderer_classes = [JSONRenderer]

    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesModelAPISerializer(notes, many=True)
        return Response(serializer.data)
