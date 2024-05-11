from django.contrib.auth.models import User
from .models import Profile
from rest_framework import status
from rest_framework.test import APITestCase


class ProfileListViewTests(APITestCase):
    """ 
    Profile creation upon registration, listing
    all profiles tests.
    """
    def setUp(self):
        gayatri = User.objects.create_user(
            username='gayatri', password='testpassword')
        sid = User.objects.create_user(
            username='sid', password='testpasswordone')
        siri = User.objects.create_user(
            username='siri', password='testpasswordtwo')

    def test_profile_created_on_user_registration(self):
        response = self.client.get('/profiles/')
        count = Profile.objects.count()
        self.assertEqual(count, 3)

    def test_can_list_profiles(self):
        response = self.client.get('/profiles/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ProfileDetailViewTests(APITestCase):
    """
    ProfileDetail view tests. Retrieve, Update and
    delete methods for authorised and unauthorised
    users tests.
    """
    def setUp(self):
        gayatri = User.objects.create_user(
            username='gayatri', password='testpassword')
        sid = User.objects.create_user(
            username='sid', password='testpasswordone')

    def test_can_retrieve_profile_using_valid_id(self):
        response = self.client.get('/profiles/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_profile_using_invalid_id(self):
        response = self.client.get('/profiles/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_logged_in_user_can_update_own_profile(self):
        self.client.login(username='gayatri', password='testpassword')
        response = self.client.put(
            '/profiles/1/', 
            {'name': 'gayatri ghogare'}
        )
        profile = Profile.objects.filter(pk=1).first()
        self.assertEqual(profile.name, 'gayatri ghogare')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logged_in_user_cant_update_other_users_profile(self):
        self.client.login(username='sid', password='testpasswordone')
        response = self.client.put(
            '/profiles/1/', {'name': 'gayatri ghogare'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_user_cant_delete_own_profile_authorised(self):
        self.client.login(username='gayatri', password='testpassword')
        response = self.client.delete('/profiles/1/')
        self.assertTrue(Profile.objects.filter(pk=1).exists())
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_user_cant_delete_other_users_profile(self):
        self.client.login(
            username='sid', password='testpasswordone')
        response = self.client.delete('/profiles/1/')
        self.assertTrue(Profile.objects.filter(pk=1).exists())
        self.assertEqual(
            response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)