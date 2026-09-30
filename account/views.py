from rest_framework import generics
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import RegisterSerializer,UserSerializer
from django.contrib.auth import get_user_model
from . permissions import IsAdmin
User=get_user_model()
# Create your views here.


class RegisterView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=RegisterSerializer
    permission_classes=[AllowAny]

class ProfileView(generics.RetrieveAPIView):
    serializer_class=UserSerializer
    permission_classes=[IsAuthenticated]
    def get_object(self):
        return self.request.user 
    
class UserListView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAdmin]    



