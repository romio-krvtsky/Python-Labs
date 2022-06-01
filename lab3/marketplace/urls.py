from django.urls import path
from .views import *

urlpatterns = [
    path('', HomePage.as_view(), name='home'),
    path('myprofile/', MyProfile.as_view(), name='my_profile'),
    path('product/<int:pk>/', ViewProduct.as_view(), name='product'),
    path('product/<int:pk>/edit', EditProduct.as_view(), name='edit_product'),
    path('product/<int:pk>/delete', DeleteProduct.as_view(), name='delete_product'),
    path('post_product/', PostProduct.as_view(), name='sell'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', LogoutUser.as_view(), name='logout'),

]
