from django.test import TestCase
from django.contrib.auth import get_user_model
from CoreApp import models


def sample_user(email='test@londonappdev.com', password='testpass'):
    return get_user_model().objects.create_user(email, password)


class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        # setup
        email = 'test@email.com'
        password = 'testpassword123'
        # execution
        user = get_user_model().objects.create_user(email, password)
        # assertion
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        # setup
        email = 'test@LONDONAPPDEV.COM'
        password = 'testpassword123'
        # exec
        user = get_user_model().objects.create_user(email, password)
        # assertion
        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, "1234")

    def test_create_new_superuser(self):
        user = get_user_model().objects.create_superuser(
            "test@testmail.com", "testpassword123")
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        tag = models.Tag.objects.create(user=sample_user(), name='vegan')
        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        ingredient = models.Ingredient.objects.create(
            user=sample_user(), name='cucumber')
        self.assertEqual(str(ingredient), ingredient.name)
