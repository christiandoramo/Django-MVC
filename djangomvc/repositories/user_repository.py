from ..models import User

class UserRepository:
    @staticmethod
    def create_user(data):
        user = User(**data)
        user.save()
        return user
