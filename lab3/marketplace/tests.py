from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from .views import *


# Create your tests here.


class TestURLS(SimpleTestCase):

    def test_home_url(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func.view_class, HomePage)

    def test_my_profile_url(self):
        url = reverse('my_profile')
        self.assertEquals(resolve(url).func.view_class, MyProfile)

    def test_post_url(self):
        url = reverse('sell')
        self.assertEquals(resolve(url).func.view_class, PostProduct)

    def test_register_url(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func.view_class, RegisterUser)

    def test_login_url(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func.view_class, LoginUser)

    def test_logout_url(self):
        url = reverse('logout')
        self.assertEquals(resolve(url).func.view_class, LogoutUser)
