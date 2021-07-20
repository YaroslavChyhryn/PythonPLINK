from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import status
from .serializers import CustomUserSerializer, RegistrationRequestSerializer, TokenSerializer
from .models import RegistrationRequest
from django.shortcuts import get_list_or_404, get_object_or_404
from rest_framework.authtoken.models import Token
from ipware import get_client_ip


class Register(APIView):
    """
    Create new user if request.data is valid.
    """
    def post(self, request, format=None):
        serializer = CustomUserSerializer(data=request.data)

        request_serializer = RegistrationRequestSerializer(data=request.data)
        client_ip, is_routable = get_client_ip(request)
        request_serializer.is_valid()
        request_serializer.validated_data['ip_address'] = client_ip
        request_serializer.save()

        if serializer.is_valid():
            serializer.validated_data['username'] = serializer.validated_data['email']
            user = serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserToken(APIView):
    """
    If user is Authenticated response his token.
    """
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, format=None):
        token = get_object_or_404(Token, user=request.user)
        data = TokenSerializer(token).data
        return Response(data, status=status.HTTP_201_CREATED)


class RequestsFromCurrentIP(APIView):
    """
    Response all registration requests from client ip address.
    """
    def get(self, request, format=None):
        client_ip, is_routable = get_client_ip(request)
        requests = get_list_or_404(RegistrationRequest.objects.filter(ip_address=client_ip).order_by('created'))
        serializer = RegistrationRequestSerializer(requests, many=True)
        return Response(serializer.data)
