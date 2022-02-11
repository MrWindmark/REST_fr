import graphene
from graphene_django import DjangoObjectType
from notesapp.models import Project, Notes
from userapp.models import User


class ProjectType(DjangoObjectType):
    class Meta:
        model = Project
        fields = ('uuid', 'name', 'repo_link', 'included_users')


class NotesType(DjangoObjectType):
    class Meta:
        model = Notes
        fields = ('title', 'inner_text', 'created_at', 'Date', 'is_complited', 'project_id')


class UserType(DjangoObjectType):
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'is_staff', 'is_active')


class Query(graphene.ObjectType):
    all_notes = graphene.List(NotesType)
    all_projects = graphene.List(ProjectType)
    all_users = graphene.List(UserType)
    notes_by_id = graphene.List(NotesType, uuid=graphene.UUID(required=True))
    projects_by_id = graphene.List(ProjectType, uuid=graphene.UUID(required=True))
    users_by_id = graphene.List(UserType, id=graphene.UUID(required=True))

    def resolve_all_notes(root, info):
        return Notes.objects.all()

    def resolve_all_projects(root, info):
        return Project.objects.all()

    def resolve_all_users(root, info):
        return User.objects.all()

    def resolve_notes_by_id(root, info, uuid):
        try:
            return Notes.objects.filter(pk=uuid)
        except Notes.DoesNotExist:
            return f'{uuid}'

    def resolve_projects_by_id(root, info, uuid):
        try:
            return Project.objects.filter(pk=uuid)
        except Project.DoesNotExist:
            return f'{uuid}'

    def resolve_users_by_id(root, info, id):
        try:
            return User.objects.filter(pk=id)
        except User.DoesNotExist:
            return f'{id}'


class ProjectMutation(graphene.Mutation):
    class Arguments:
        uuid = graphene.String(required=True)
        name = graphene.String(required=False)
        repo_link = graphene.String(required=False)

    project = graphene.Field(ProjectType)

    @classmethod
    def mutate(cls, root, info, name, repo_link, uuid):
        project = Project.objects.get(pk=uuid)
        if name:
            project.name = name
        if repo_link:
            project.repo_link = repo_link
        project.save()
        return ProjectMutation(project=project)


class Mutation(graphene.ObjectType):
    update_project = ProjectMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)

#
# class Query(graphene.ObjectType):
#     hello = graphene.String(default_value="Hi!")
#
#
# schema = graphene.Schema(query=Query)
