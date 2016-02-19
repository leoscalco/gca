# -*- coding: utf-8 -*-
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from models import *


def get_in(request):
	user = authenticate(username=request.POST.get('username'), password=request.POST.get('password'))
	if user is not None:
	    # the password verified for the user
	    if user.is_active:
	    	login(request, user)
	        context = "User is valid, active and authenticated"
	        return HttpResponseRedirect('/gestao/scenario')
	    else:
	        context = "The password is valid, but the account has been disabled!"
	else:
	    # the authentication system was unable to verify the username and password
	    return HttpResponse(u"Login não efetuado! Usuário não autenticado.")

def get_out(request):
	logout(request)
	return HttpResponseRedirect('/gestao')

def change_pass(request):
    thisUser = request.POST.get('username')
    senha1 = request.POST.get('password')
    senha2 = request.POST.get('password2')
    if thisUser == request.user.email:
        if senha1 == senha2:
            estudante = Student.objects.get(email=request.user.email)
            estudante.set_password(senha1)
            estudante.save()
            return HttpResponseRedirect("/gestao")
        else:
            context = {'user': request.user,
                       'message': "Senhas não são iguais"}
    	    return render(request, 'gestao/user/change_pass.html', context)