from django.test import TestCase
from core.models import *
from django.contrib.auth import get_user_model


""" Note: """

class ModelTests(TestCase):

    """Test models."""
    def test_create_user_with_email_successful(self):
        """Test creating a user with an email is successful."""
        email = 'zing@example.com'
        password = 'password'
        user = User.objects.create_user(
            email = email,
            password = password,
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))


    def test_new_user_email_normalised(self):
        """Test email is normalised for new users."""
        sample_emails = [
            ['test1@EXAMPLE.com','test1@example.com'],
            ['Test2@Example.com','Test2@example.com'],
            ['TEST3@EXAMPLE.com','TEST3@example.com'],
            ['test4@example.COM','test4@example.com'],
        ]

        for email, expected in sample_emails:
            user = User.objects.create_user(email, 'sample123')
            self.assertEqual(user.email, expected)

    def test_new_user_without_email_aises_error(self):
        """Test that creating a user without an email raises a valueerror."""
        with self.assertRaises(ValueError):
            User.objects.create_user('', 'test123')

    def test_create_superuser(self):
        """Test creating a superuser."""
        user = User.objects.create_superuser(
            'test@example.com',
            'test123',
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
