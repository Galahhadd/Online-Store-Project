from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages

from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.token_blacklist.models import BlacklistedToken, OutstandingToken

from .forms import CustomUserCreationForm, CustomLoginForm
from .serializers import (
	RegisterUserSerializer,
	CustomUserSerializer,
	ChangePasswordSerializer,
	UpdateProfileSerializer,
	)
from .models import CustomUser



class RegisterApiView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer


class GetCurrentUserView(APIView):
	permission_classes = (IsAuthenticated,)

	def get(self, request):
		user = request.user
		serializer = CustomUserSerializer(user)
		return Response(serializer.data)


class ChangePasswordView(generics.UpdateAPIView):
	queryset = CustomUser.objects.all()
	permission_classes = (IsAuthenticated,)
	serializer_class = ChangePasswordSerializer

	def get_object(self):
		return CustomUser.objects.get(pk=self.request.user.id)


class UpdateProfileView(generics.UpdateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = UpdateProfileSerializer

    def get_object(self):
    	return CustomUser.objects.get(pk=self.request.user.id)

class LogoutView(APIView):
	permission_classes = (IsAuthenticated,)

	def post(self, request):

		try:
			refresh_token = request.data['refresh_token']
			token = RefreshToken(refresh_token)
			token.blacklist()

			return Response(status=status.HTTP_205_RESET_CONTENT)
		except Exception:
			return Response(status=status.HTTP_400_BAD_REQUEST)






def register_view(request):
	if request.user.is_authenticated:
		messages.info(request, 'You are already have account')
		return redirect('store:home')

	if request.method == "POST":
		form = CustomUserCreationForm(request.POST)
		if form.is_valid():
			user = form.save(commit=False)
			user.is_active = True
			user.save()
			return (redirect('store:home'))

		else:
			context = {
				'form': form,
				'form_errors': form.errors
				}
			return render(request, 'register.html', context)

	form = CustomUserCreationForm()
	return render(request, 'register.html', {'form': form})



def login_view(request):
	if request.user.is_authenticated:
		messages.info(request, 'You are already logged in')
		return redirect('store:home')

	if request.method == "POST":
		form = CustomLoginForm(request.POST)
		print(request.POST)
		if form.is_valid():
			email = form.cleaned_data['email']
			password = form.cleaned_data['password']

			user = authenticate(request, email=email, password=password)

			if user is not None:
				login(request, user)
				return redirect('store:home')
			else:
				messages.error(request, 'Invalid email or password')
				return redirect('accounts:login')

		else:
			messages.error(request, 'Invalid form data')
			return redirect('accounts:login')

	form = CustomLoginForm()
	return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    return redirect('store:home')
