from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import generics, permissions

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import check_password

from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

from django.views import View

from user.serializers import ChangePasswordSerializer, UserSerializer

# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_info(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


class UpdateUserView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return User.objects.all()

    def get_object(self):
        return self.request.user


""" class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            # Vérifier l'ancien mot de passe
            if not check_password(old_password, user.password):
                return Response({'error': 'Ancien mot de passe incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

            # Vérifier si le nouveau mot de passe correspond à la confirmation
            if new_password != confirm_password:
                return Response({'error': 'Le nouveau mot de passe ne correspond pas à la confirmation.'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Mettre à jour le mot de passe de l'utilisateur
            user.set_password(new_password)
            user.save()

            return Response({'success': 'Mot de passe mis à jour avec succès.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) """



class ChangePasswordView(View):
    permission_classes = [IsAuthenticated]

    @swagger_auto_schema(
    method='put',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'old_password': openapi.Schema(type=openapi.TYPE_STRING),
            'new_password': openapi.Schema(type=openapi.TYPE_STRING),
            'confirm_password': openapi.Schema(type=openapi.TYPE_STRING),
        },
        required=['old_password', 'new_password', 'confirm_password'],
    ),
    responses={200: 'Mot de passe mise à jour avec succès'}
    )
    @api_view(['PUT'])
    def putPassword(request):
        serializer = ChangePasswordSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user
            old_password = serializer.validated_data['old_password']
            new_password = serializer.validated_data['new_password']
            confirm_password = serializer.validated_data['confirm_password']

            # Vérifier l'ancien mot de passe
            if not check_password(old_password, user.password):
                return Response({'error': 'Ancien mot de passe incorrect.'}, status=status.HTTP_400_BAD_REQUEST)

            # Vérifier si le nouveau mot de passe correspond à la confirmation
            if new_password != confirm_password:
                return Response({'error': 'Le nouveau mot de passe ne correspond pas à la confirmation.'},
                                status=status.HTTP_400_BAD_REQUEST)

            # Mettre à jour le mot de passe de l'utilisateur
            user.set_password(new_password)
            user.save()

            return Response({'success': 'Mot de passe mis à jour avec succès.'}, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)