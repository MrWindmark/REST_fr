import datetime
import json
from uuid import uuid4

from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIRequestFactory, force_authenticate, APIClient, APISimpleTestCase, APITestCase
from mixer.backend.django import mixer
# from django.contrib.auth.models import User
from userapp.models import User
from notesapp.views import ProjectModelViewSet
from notesapp.models import Project, Notes


# Create your tests here.
class TestProjectViewSet(TestCase):

    def test_get_list(self):
        factory = APIRequestFactory()
        request = factory.get('/api/projects/')
        view = ProjectModelViewSet.as_view({'get': 'list'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_project_unautorized(self):
        factory = APIRequestFactory()
        user = User.objects.create_user('testMan', 'test@example.com', 'zero_security')
        request = factory.post('/api/projects/', {'uuid': uuid4(), 'name': 'Test Project', 'repo_link': 'nolink4.us',
                                                  'included_users': user})
        # force_authenticate(request, user)
        view = ProjectModelViewSet.as_view({'post': 'create'})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_project_admin(self):
        user = User.objects.create_user('testMan', 'test@example.com', 'zero_security')
        test_uuid = uuid4()
        project = Project.objects.create(uuid=test_uuid, name='Test Project', repo_link='nolink4.us')
        admin = User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
        client = APIClient()
        client.login(username='admin', password='admin')
        response = client.get('/api/projects/')
        test_project = Project.objects.get(uuid=test_uuid)
        self.assertEqual(test_project.name, 'Test Project')

    def test_create_project_user(self):
        user = User.objects.create_user('testMan', 'test@example.com', 'zero_security')
        test_uuid = uuid4()
        project = Project.objects.create(uuid=test_uuid, name='New Test Project', repo_link='well.com')
        client = APIClient()
        client.login(username='testMan', password='zero_security')
        response = client.get('/api/projects/')
        test_project = Project.objects.get(uuid=test_uuid)
        client.logout()
        self.assertEqual(test_project.name, 'New Test Project')

    def test_create_project_user_failed(self):
        user = User.objects.create_user('testMan', 'test@example.com', 'zero_security')
        test_uuid = uuid4()
        project = Project.objects.create(uuid=test_uuid, name='New Test Project', repo_link='well.com')
        client = APIClient()
        client.login(username='testMan', password='zero_security')
        response = client.get('/api/projects/')
        client.logout()
        test_project = Project.objects.get(uuid=test_uuid)
        self.assertEqual(test_project.name, 'New Test Project')


class TestNoteViewSet(APITestCase):

    def test_notes_list(self):
        admin = User.objects.create_superuser('admin', 'admin@admin.admin', 'admin')
        user = User.objects.create_user('testMan', 'test@example.com', 'zero_security')
        test_uuid = uuid4()
        project = Project.objects.create(uuid=test_uuid, name='New Test Project', repo_link='well.com')
        note_uuid = uuid4()
        note = Notes.objects.create(
            uuid=note_uuid,
            title='Test Title',
            inner_text='Some inner text',
            is_complited=True,
            project_id=project,
            creator=user,
            created_at=datetime.date.today(),
            updated_at=datetime.date.today()
        )

        req_token = self.client.post('/api/token/', {'username': 'admin', 'password': 'admin'})
        access_token = req_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)
        response = self.client.get('/api/notes/')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_note = Notes.objects.get(uuid=note_uuid)
        self.assertEqual(test_note.project_id, project)

    def test_note_mixer_list(self):
        note = mixer.blend(Notes, title='Hello there!', inner_text='General Kenobi')
        user = User.objects.create_user('testMan', 'test@example.com', 'zero_security')

        req_token = self.client.post('/api/token/', {'username': 'testMan', 'password': 'zero_security'})
        access_token = req_token.data['access']
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + access_token)

        response = self.client.get('/api/notes/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        test_note = Notes.objects.get(title='Hello there!')
        self.assertEqual(test_note.inner_text, 'Hello there!', msg='GENERAL KENOBI!')
