# from django.shortcuts import render

from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .services.user_service import UserService
from django.core.exceptions import ValidationError
import json

@method_decorator(csrf_exempt, name='dispatch')  # Exemplo sem CSRF para testes. Remova para produção.
class UserCreateView(View):
    def post(self, request, *args, **kwargs):
        try:
            print("entrou")
            data = json.loads(request.body)
            user = UserService.create_user(data)
            return JsonResponse({"status": "success", "message": "User created successfully", "id": str(user.id)}, status=201)
        except ValidationError as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": "An error occurred"}, status=500)


@method_decorator(csrf_exempt, name='dispatch')  # Exemplo sem CSRF para testes. Remova para produção.
class HelloWorld(View):
    def get(self, request, *args, **kwargs):
        try:
            return JsonResponse({"status": "success", "message": "Hello World!"}, status=200)
        except ValidationError as e:
            return JsonResponse({"status": "error", "message": str(e)}, status=400)
        except Exception as e:
            return JsonResponse({"status": "error", "message": "An error occurred"}, status=500)