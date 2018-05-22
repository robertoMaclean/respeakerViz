# accounts/views.py
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth import authenticate, get_user_model, login, logout, update_session_auth_hash
from django.shortcuts import render, redirect
from .forms import UserLoginForm, UserRegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm

def login_view(request):
	logout(request)
	title = "Ingresar"
	next = request.GET.get('next')
	form = UserLoginForm(request.POST or None)
	if form.is_valid():
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get("password")
		user = authenticate(username=username, password=password)
		login(request, user)
		if next:
			return redirect(next)
		return redirect(reverse_lazy("save_file"))
	return render(request, "form.html", {"form":form, "title":title})

def register_view(request):
	if not request.user.is_authenticated:
		title = "Registrarse"
		form = UserRegisterForm(request.POST or None)
		if form.is_valid():
			user = form.save(commit=False)
			password = form.cleaned_data.get('password')
			user.set_password(password)
			user.save()
			# new_user = authenticate(username=user.username, password=password)
			# login(request, new_user)
			messages.success(request, 'Tu cuenta se ha creado satisfactoriamente. Ahora puedes acceder a tu cuenta.')
			return redirect(reverse_lazy("save_file"))
		context = {
			"form": form,
			"title": title
		}

		return render(request, "form.html", context)
	return redirect(reverse_lazy("save_file"))

@login_required(redirect_field_name='login')
def logout_view(request):
	logout(request)
	return redirect(reverse_lazy("login"))

@login_required(redirect_field_name='login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)  # Important!
            messages.success(request, 'Tu contraseña ha sido cambiada correctamente!')
            return redirect('/')
        else:
            messages.error(request, 'Corrija el error.')
    else:
        form = PasswordChangeForm(request.user)
    return render(request, 'change_password.html', {
        'form': form
    })
