from rest_framework import serializers # type: ignore

class UserSerializer(serializers.Serializer):
    name = serializers.CharField(required=False, max_length=100, allow_blank=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(write_only=True, required=True)

    def create(self, validated_data):
        return validated_data  # O serviço cuidará da criação
