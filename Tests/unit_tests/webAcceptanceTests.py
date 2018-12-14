from django.test import TestCase, Client
from django.urls import reverse
from TAServer.models import Staff, Course, Section
from Managers.userManager import UserManager as UM
from Managers.DjangoStorageManager import DjangoStorageManager as ds


class ViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        adminUser = {"username":"Admin", "password": "Admin103", "role" :"Administrator"}
        self.storage = ds()
        user = UM(self.storage)
        user.add(adminUser)
        pass

    def tearDown(self):
        pass

    def test_urls(self):
        response = self.client.get('/about/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/FAQ/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/courses/add')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/sections/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/sections/add')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/user/view/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/user/add/')
        self.assertEqual(response.status_code, 200)
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 200)

    def test_login_Again(self):
        response = self.client.post(reverse('login'), data={'username': 'Admin', 'password': 'Admin103'}, follow=True)

        # Check our user is logged in
        self.assertEqual(str(response.context['user']), 'Admin')
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)

        # Successful login should redirect to home page
        self.assertRedirects(response, '/home/')
        self.client.logout()
