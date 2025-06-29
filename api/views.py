from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from .mock_data import PROFILE, USAGE
from .serializers import LoginSerializer, APIUsageSerializer
import logging
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from rest_framework.renderers import JSONRenderer, TemplateHTMLRenderer





class LoginView(APIView):
    renderer_classes = [TemplateHTMLRenderer, JSONRenderer]

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        is_json = request.content_type == 'application/json'
        data = request.data if is_json else request.POST

        serializer = LoginSerializer(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']

            user = authenticate(username=username, password=password)

            if user:
                if user:
                    login(request, user)
                    token, _ = Token.objects.get_or_create(user=user)
                    if is_json:
                        return Response({'token': token.key}, status=200)
                    else:
                        return redirect('profile')
            else:
                if is_json:
                    return Response({'error': 'Invalid credentials'}, status=401)
                return render(request, 'login.html', {'error': 'Invalid credentials'})

        if is_json:
            return Response(serializer.errors, status=400)
        return render(request, 'login.html', {'errors': serializer.errors})


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'profile.html', {'profile': PROFILE})


class APIUsageView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return render(request, 'usage.html', {'usage': USAGE})

    def post(self, request):
        serializer = APIUsageSerializer(data=request.data)
        if serializer.is_valid():
            new_entry = serializer.validated_data
            logging.info(f"[Kafka Simulation] New usage: {new_entry}")
            return Response({"status": "added", "data": new_entry}, status=201)
        return Response(serializer.errors, status=400)
