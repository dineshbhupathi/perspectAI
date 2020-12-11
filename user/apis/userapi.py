from rest_framework import viewsets, status
from ..models import *
from ..serializers.userserializer import *
import jwt
from rest_framework_jwt.serializers import jwt_payload_handler
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth import login, authenticate
from rest_framework import permissions
from user.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class UserCreationApi(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer


class EmployeeCreation(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    def list(self, request, *args, **kwargs):
        print(request.user.id)
        queryset = Employee.objects.filter(hr__user_id=request.user.id)
        print(queryset,'query')
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)




class Login(APIView):
    def post(self, request):
        print(request.GET.get('username'),'kkkk')
        if not request.data:
            return Response({'Error': "Please provide username/password"}, status="400")
        username = request.data['username']
        password = request.data['password']
        try:
            user = authenticate(username=username, password=password)
        except User.DoesNotExist:
            return Response({'Error': "Invalid username/password"}, status="400")
        if user:
            login(request, user)
            token, _ = Token.objects.get_or_create(user=user)
            return Response({'token': token.key},
                                status=status.HTTP_200_OK)
        else:
            res = {
                'error': 'can not authenticate with the given credentials or the account has been deactivated'}
            return Response(res, status=status.HTTP_403_FORBIDDEN)