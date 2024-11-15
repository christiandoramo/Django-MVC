from ..repositories.user_repository import UserRepository
from django.core.exceptions import ValidationError
from django.contrib.auth.hashers import make_password

class UserService:
    @staticmethod
    def create_user(data):
        if 'email' not in data or 'password' not in data:
            raise ValidationError("Email and password are required fields.")
        
        # Validações adicionais de tipos (como em TypeScript)
        if not isinstance(data.get('email'), str):
            raise ValidationError("Email must be a string.")
        if not isinstance(data.get('password'), str):
            raise ValidationError("Password must be a string.")
        if 'name' in data and not isinstance(data.get('name'), str):
            raise ValidationError("Name must be a string if provided.")

        # Criptografando a senha
        data['password'] = make_password(data['password'])

        # Chama o repositório para salvar o usuário
        return UserRepository.create_user(data)
