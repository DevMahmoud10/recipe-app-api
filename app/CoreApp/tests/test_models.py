from django.test import TestCase
from django.contrib.auth import get_user_model

class ModelTests(TestCase):

    def test_create_user_with_email_successful(self):
        #setup
        email = 'test@email.com'
        password = 'testpassword123'
        #execution
        user = get_user_model().objects.create(
            email=email,
            password=password
        )
        #assertion
        self.assertEqual(user.email, email)
        self.assertEqual(user.password,password)
    