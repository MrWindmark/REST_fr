from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet, ViewSet
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination

# Create your views here.
from notesapp.models import Project, Notes
# serializers for V2
from notesapp.serializers import ProjectsModelSerializer, NotesModelSerializer
# serializers for V3
from notesapp.serializers import BaseProjectsModelSerializer, BaseNotesModelSerializer
# serializers for V1 (urls not in use)
from notesapp.serializers import ProjectsModelAPISerializer, NotesModelAPISerializer


# v1
class ProjectModelViewAPISet(APIView):
    renderer_classes = [JSONRenderer]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectsModelAPISerializer(projects, many=True)
        return Response(serializer.data)


# v2.1
class ProjectModelViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = BaseProjectsModelSerializer
    permission_classes = (IsAuthenticatedOrReadOnly,)

    def get_serializer_class(self):
        if self.request.version == 1:
            return ProjectsModelSerializer
        return BaseProjectsModelSerializer


# v1.3
# class ProjectViewSet(ViewSet):
#     renderer_classes = [JSONRenderer]
#
#     def list(self, request):
#         queryset = Project.objects.all()
#         context = {'request': request}
#         serializer = ProjectsModelSerializer(queryset, context=context, many=True)
#         return Response(serializer.data)
#
#     def retrieve(self, request, pk=None):
#         queryset = get_object_or_404(Project, pk=pk)
#         context = {'request': request}
#         serializer = ProjectsModelSerializer(queryset, context=context)
#         return Response(serializer.data)

# v2
class NoteModelViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    serializer_class = BaseNotesModelSerializer
    filterset_fields = ['title', 'creator']

    def get_serializer_class(self):
        print(self.request.version)
        if self.request.version == 1:
            return NotesModelSerializer
        return BaseNotesModelSerializer


# v1.3
# class NoteModelListViewAPISet(APIView):
#     renderer_classes = [JSONRenderer]
#     # queryset = Notes.objects.all()
#     # serializer_class = NotesModelAPISerializer
#     permission_classes = [IsAuthenticated]
#
#     def get(self, request):
#         notes = Notes.objects.all()
#         serializer = NotesModelAPISerializer(notes, many=True)
#         return Response(serializer.data)


# v3
class NoteModelCreateViewAPISet(CreateAPIView):
    renderer_classes = [JSONRenderer]
    queryset = Notes.objects.all()
    serializer_class = NotesModelAPISerializer


class NotesLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 10


class NotesLimitOffsetPaginatonViewSet(ModelViewSet):
    queryset = Notes.objects.all()
    serializer_class = NotesModelSerializer
    pagination_class = NotesLimitOffsetPagination
