from django.contrib.auth import get_user_model
from rest_framework import serializers

User=get_user_model()

class RegisterSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True)

    class Meta:
        model=User
        fields=['username',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'role',]
        def create(self , validated_data):
            password=validated_data.pop('password')
            user=User.objects.create_user(
                password=password, **validated_data
            )

            return User
        
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['id', 'username',
            'email',
            'password',
            'first_name',
            'last_name',
            'phone',
            'role',]        