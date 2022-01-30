import django_filters.rest_framework
from rest_framework.generics import ListAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
from notesapp.models import Project, Notes
from notesapp.serializers import ProjectsModelSerializer, NotesModelSerializer
from notesapp.serializers import ProjectsModelAPISerializer, NotesModelAPISerializer
from notesapp.permissions import StaffOnly


class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectsModelSerializer
    permission_classes = (IsAuthenticated,)


class NoteModelViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer
    filterset_fields = ['title', 'creator']


class ProjectModelViewAPISet(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectsModelAPISerializer(projects, many=True)
        return Response(serializer.data)


class NoteModelListViewAPISet(APIView):
    renderer_classes = [JSONRenderer]
    # queryset = Notes.objects.all()
    # serializer_class = NotesModelAPISerializer
    permission_classes = [IsAuthenticated]

    def get(self, request):
        notes = Notes.objects.all()
        serializer = NotesModelAPISerializer(notes, many=True)
        return Response(serializer.data)


class NoteModelCreateViewAPISet(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Notes.objects.all()
    serializer_class = NotesModelAPISerializer


class ProjectViewSet(ViewSet):
    renderer_classes = [JSONRenderer]

    def list(self, request):
        queryset = Project.objects.all()
        context = {'request': request}
        serializer = ProjectsModelSerializer(queryset, context=context, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = get_object_or_404(Project, pk=pk)
        context = {'request': request}
        serializer = ProjectsModelSerializer(queryset, context=context)
        return Response(serializer.data)


class NotesLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 3


class NotesLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer
    pagination_class = NotesLimitOffsetPagination
