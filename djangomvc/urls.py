from django.urls import path
from .views import HelloWorld, UserCreateView

urlpatterns = [
    path('create-user/', UserCreateView.as_view(), name='create_user'),
    path('hello-world/', HelloWorld.as_view(), name='hello_world'),
    # Outras URLs do seu app
]



