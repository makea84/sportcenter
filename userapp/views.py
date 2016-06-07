from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template.context_processors import csrf
from django.http import JsonResponse

from userapp.forms import UserAppForm, UserForm
from userapp.models import UserApp

from utils.auxiliar import get_error, check_user, getAllObjects

import logging
from court.models import Court
from classroom.models import Classroom
from product.models import Product
from machine.models import Machine

logger = logging.getLogger('sportcenter.page_processors')

def get_user(user):
    usuario = User.objects.get(pk=user)
    return usuario

def index(request):
    diccionario = {}
    diccionario.update(csrf(request))
    if request.method == 'POST' and request.is_ajax():   
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)
        email = request.POST.get('email', None)
        dni = request.POST.get('dni', None)
        name = request.POST.get('name', None)
        crear = request.POST.get('crear',None)
        logger.debug('index')
        logger.debug(crear)
        logger.debug(request.POST)
        formU = UserAppForm(request.POST)
        formUC = UserForm(request.POST)
        formA = AuthenticationForm(request, request.POST)
        logger.debug(formA)
        if crear=='crear':
            if formUC.is_valid() and formU.is_valid():
                logger.debug('formUC formU ok')
                user = User.objects.create_user(username=username, email=email, password=password)
                #user.set_password(password)
                user.save()
                userApp = UserApp.objects.create(user=user, dni=dni, name=name)
                userApp.save()
                response_data = {'Usuario':'Ha sido creado un nuevo usuario.'}
                return JsonResponse(response_data)
            else:
                logger.debug('invalid')
                response_data = get_error(formUC)
                response_data.update(get_error(formU))
                logger.debug(response_data)
                return JsonResponse(response_data)
        if crear=='login':
            logger.debug(formA)
            logger.debug(username)
            logger.debug(password)
            username = str(request.POST['username'])
            password = str(request.POST['password'])
            logger.debug(formA.is_valid())
            if formA.is_valid():
                logger.debug('ok_login')
                acceso = authenticate(username=username, password=password)
                logger.debug(acceso)
                if acceso is not None:
                    if acceso.is_active:
                        login(request, acceso)
                        logger.debug('redirect ok')
                        response_data={'url':'/sportcenter/home/'}
                        return JsonResponse(response_data)
                    else:
                        logger.debug('no activo')
                        response_data={'Acceso':'No tiene acceso activo.'}
                        return JsonResponse(response_data)
                else:
                    logger.debug('no access')
                    response_data={'Acceso':'No existe usuario.'}
                    return JsonResponse(response_data)
            else:
                logger.debug('formA no ok')
                response_data={'hay_error':True,'Error':'Rellene los campos.'}
                logger.debug(response_data)
                return JsonResponse(response_data)
    else:
        formA = AuthenticationForm()
        formU = UserAppForm()
        formUC = UserForm()
        logger.debug('no POST')
        diccionario.update({'formA': formA, 'formU': formU, 'formUC': formUC})
    return render_to_response('userapp/index.html', diccionario)

@login_required(login_url='/sportcenter/')
def log_user_out(request):
    logout(request)
    return redirect('/sportcenter/')

def home(request):
    diccionario=check_user(request)
    diccionario.update({'pista':getAllObjects(Court,request)})
    diccionario.update({'clase':getAllObjects(Classroom,request)})
    diccionario.update({'producto':getAllObjects(Product,request)})
    diccionario.update({'maquina':getAllObjects(Machine,request)})
    return render_to_response('userapp/home.html', diccionario)
