from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render_to_response
from django.contrib.auth.models import User
from django.template.context_processors import csrf
from django.http import HttpResponseRedirect

from userapp.forms import UserAppForm, UserForm
from userapp.models import UserApp

import logging
logger = logging.getLogger('sportcenter.page_processors')


def index(request):
    # csrf=request.POST.get('csrfmiddlewaretoken',None)
    diccionario = {}
    diccionario.update(csrf(request))
    username = request.POST.get('username', None)
    password = request.POST.get('password', None)
    email = request.POST.get('email', None)
    dni = request.POST.get('dni', None)
    name = request.POST.get('name', None)
    logger.debug('index')
    logger.debug(request.POST)
    if request.method == 'POST':
        logger.debug('POST-')
        formU = UserAppForm(request.POST)
        formUC = UserForm(request.POST)
        formA = AuthenticationForm(request.POST)
        if formUC.is_valid and formU.is_valid():
            logger.debug('formUC formU ok')
            user = User.objects.create(username=username, email=email)
            user.set_password(password)
            user.save()
            userApp = UserApp.objects.create(idUser=user, dni=dni, name=name)
            userApp.save()
            diccionario.update(csrf(request))
            diccionario.update(
                {'formA': formA, 'formU': formU, 'formUC': formUC})
            logger.debug('redirect')
            return HttpResponseRedirect('/sportcenter/')
        else:
            diccionario.update(csrf(request))
            logger.debug('formUC formU no ok')
            error = 'Errores'
            diccionario.update({
                'formA': formA, 'formU': formU, 'formUC': formUC,
                'error': error})
        if formA.is_valid:
            logger.debug('ok_login')
            acceso = authenticate(username=username, password=password)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    logger.debug('redirect ok')
                    return HttpResponseRedirect('/sportcenter/home/')
                else:
                    logger.debug('no activo')
                    diccionario.update({
                        'formA': formA, 'formU': formU, 'formUC': formUC})
                    return HttpResponseRedirect('/sportcenter/')
            else:
                logger.debug('no access')
                diccionario.update({
                    'formA': formA, 'formU': formU, 'formUC': formUC})
                return HttpResponseRedirect('/sportcenter/')
        else:
            logger.debug('formA no ok')
            diccionario.update(csrf(request))
            diccionario.update({
                'formA': formA, 'formU': formU, 'formUC': formUC})
            return HttpResponseRedirect('/sportcenter/')
    else:
        formA = AuthenticationForm()
        formU = UserAppForm()
        formUC = UserForm()
        logger.debug('no POST')
    diccionario.update(csrf(request))
    diccionario.update({'formA': formA, 'formU': formU, 'formUC': formUC})
    return render_to_response('main/index.html', diccionario)


@login_required(login_url='/sportcenter/')
def logout(request):
    logout(request)
    return redirect('index')


@login_required(login_url='/sportcenter/')
def home(request):
    diccionario = {'logueado': request.user}
    return render_to_response('main/home.html', diccionario)
