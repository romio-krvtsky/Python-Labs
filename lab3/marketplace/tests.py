from django.test import TestCase
from django.test import SimpleTestCase
from django.urls import reverse, resolve

from .models import User, Product
from .views import HomePage, MyProfile, PostProduct, RegisterUser, LoginUser, LogoutUser


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


class ProductTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(
            username='smbd',
            email='smbd@gmail.com',
            password='123456',
            phone='+3753330906',
        )
        self.product = Product.objects.create(
            name='smth',
            description='very good',
            price=423,
            owner=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.username)
        self.assertEqual(str(self.product), self.product.name)

    def test_product(self):
        self.assertEqual(f'{self.product.name}', 'smth')
        self.assertEqual(f'{self.product.description}', 'very good')
        self.assertEqual(f'{self.product.price}', '423')
        self.assertEqual(f'{self.product.owner}', 'smbd')

    def test_product_detail_view(self):
        response = self.client.get(reverse('product', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'marketplace/product.html')

    def test_product_edit_view(self):
        response = self.client.post(reverse('edit_product', kwargs={'pk': self.product.pk}), {
            'description': 'new abcd',
        })
        self.assertEqual(response.status_code, 200)

    def test_product_delete_view(self):
        response = self.client.post(reverse('delete_product', kwargs={'pk': self.product.pk}))
        self.assertEqual(response.status_code, 302)

    def test_product_create_view(self):
        response = self.client.post(reverse('sell'), {
            'name': 'name',
            'description': 'description',
            'price': 423,
            'owner': self.user,
        })
        self.assertEqual(response.status_code, 302)
