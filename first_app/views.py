from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Apartment
from .forms import AptForm, LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def index(request):
	apartments = Apartment.objects.all()
	form = AptForm()
	return render(request, 'index.html', {
		'apartments': apartments,
		'form': form
	})


def detail(request, apt_id):
	apartment = Apartment.objects.get(id=apt_id)
	return render(request, 'detail.html', {'apartment': apartment})


def user(request, username):
	user_data = User.objects.get(username=username)
	user_apt = Apartment.objects.filter(user=user_data)
	return render(request, 'user.html', {'user': user_data, 'apt': user_apt})


def logout_view(request):
	logout(request)
	return HttpResponseRedirect('/')


def login_view(request):
	if request.method == 'POST':
		form = LoginForm(request.POST)
		if form.is_valid():
			u = form.cleaned_data['username']
			p = form.cleaned_data['password']
			user_d = authenticate(username=u, password=p)
			if user_d is not None:
				if user_d.is_active:
					login(request, user_d)
					return HttpResponseRedirect('/')
				else:
					print('User is inactive')
			else:
				print('Credentials incorrect')
	else:
		form = LoginForm()
		return render(request, 'login.html', {'form': form})


def post_apt(request):
	form = AptForm(request.POST, request.FILES)
	if form.is_valid():
		apt = form.save(commit=False)
		apt.user = request.user
		apt.save()
	return HttpResponseRedirect('/')
