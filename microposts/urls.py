from django.urls import path
from .views import CustomSignUpView, WallView, CreatePostView
from django.contrib.auth.views import LoginView, LogoutView

# Definir el nombre de la aplicacion
app_name = 'microposts'

urlpatterns = [
    path("register/", CustomSignUpView.as_view(), name="register"),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('', WallView.as_view(), name="home"),
    path('posts/create/', CreatePostView.as_view(), name="create_post")
]