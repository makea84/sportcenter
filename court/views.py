from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import CourtForm, ReservationForm, ReservateForm
from .models import Court, Reservation

from utils.auxiliar import delete, edit, get_error, get_data, get_data_reverse, get_data_dict,\
    get_data_dict_reverse, check_user, getAllObjects

import logging
import collections


logger = logging.getLogger('sportcenter.page_processors')

def get_all(request):
    data = Reservation.objects.filter(user=request.user)
    paginator = Paginator(data, 2)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    data
    return data

def select_operation(request, text, operation, texto):
    """Select the operation to be done.
    :param text: Type of the element to operate.
    :type text: Object
    :param request: A Request instance.
    :param operation: Operation to be done.
    :type operation: String
    :param texto: Select type of element
    :type texto: String
    :return: form of the type select
    """
    if operation == 'update':
        id_element = request.POST.get('element', None)
        logger.debug(id_element)
        instance = get_object_or_404(text, pk=id_element)
        logger.debug(instance)
        if texto == 'court':
            form = CourtForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'reservation':
            form = ReservationForm(request.POST or None, request.FILES or None, instance=instance)
    if operation == 'create':
        if texto == 'court':
            form = CourtForm(request.POST or None, request.FILES or None)
        if texto == 'reservation':
            form = ReservationForm(request.POST or None, request.FILES or None)
    return form

def retrieve(request, text, pk):
    """Retrieve a element in the system.
    :param text: Type of the element to get.
    :type text: Object
    :param request: A Request instance.
    :param pk: The primary key of the element.
    :type pk: Int
    :return: dictionary with the the element
    """
    obj = text.objects.get(pk=pk)
    logger.debug(obj)
    if text is Court:
        imagen = obj.image.path.split('/')
        imagen = imagen[len(imagen)-2]+'/'+imagen[len(imagen)-1]
        diccion = {'image':imagen}
        dicti = collections.OrderedDict(diccion)
        logger.debug(dicti)
        dicti.update(model_to_dict(obj, exclude=['image']))
        logger.debug(dicti)
        return get_data_dict(dicti)
    return get_data_dict(model_to_dict(obj))

def get_other_user(request):
    """Load data for user template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Court, request)
    dictionary={'pista':data}
    data = getAllObjects(Reservation, request)
    dictionary.update({'reserva':data})
    return render(request,"court/prueba.html", dictionary)

def get_court(request):
    """Load court data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Court, request)
    dictionary={'pista':data}
    return render(request,"court/admin/prueba_pista.html", dictionary)

def get_reservation(request):
    """Load reservation data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Reservation, request)
    dictionary={'reserva':data}
    return render(request,"court/admin/prueba_reserva.html", dictionary)

def get_reservation_form(request):
    """Reload reservation form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_reservations = ReservationForm()
    dictionary = {'form_reservations':form_reservations}
    return render(request,"court/admin/load_reservation.html", dictionary)

def create(request, tipe, operation, text):
    """Create a element in the system.
    :param tipe: Type of the element to be create.
    :type tipe: Object
    :param request: A Request instance.
    :param operation: select to be done
    :type operation: String
    :param text: select the tipe of element
    :type text: String
    :return: dictionary with the state of the element
    """
    logger.debug(operation)
    logger.debug(tipe)
    logger.debug(text)
    data = get_data(request) 
    data_reverse = get_data_reverse(data)
    logger.debug(data)
    form = select_operation(request, tipe, operation, text)
    if form.is_valid():
        logger.debug('valid')
        if tipe is Court:
            data_reverse['image'] = form.cleaned_data['image']
        if tipe is Reservation:
            data_reverse['user'] =  User.objects.get(pk=int(data_reverse['user']))
            data_reverse['court'] = Court.objects.get(pk=data_reverse['court'])
        obj = tipe.objects.create(**data_reverse)
        obj.save()
        logger.debug(obj)
        return retrieve(request, tipe, obj.pk)
    else:
        logger.debug('invalid')
        response_data = get_error(form)
        return response_data
    
def change(request, text, operation, texto):
    """Update a element in the system.
    :param tipe: Type of the element to be create.
    :type tipe: Object
    :param request: A Request instance.
    :param operation: select to be done
    :type operation: String
    :param text: select the tipe of element
    :type text: String
    :return: dictionary with the state of the element
    """
    form = select_operation(request, text, operation, texto)
    logger.debug(form)
    if form.is_valid():
        logger.debug('valid')
        form.save()
        data = get_data(request)
        return data
    else:
        logger.debug('invalid')
        response_data = get_error(form)
        return response_data

def allCourts(request):
    """Process the view for court and call other functions and methods
    :param request: A Request instance.
    """
    dicti=check_user(request)
    logger.debug(dicti)
    key = request.POST.get('pk', None)
    text = request.POST.get('tipe', None)
    dicti.update({'pista':getAllObjects(Court, request)})
    if 'admin' in dicti:
        dicti.update({'reserva':getAllObjects(Reservation, request)})
    if 'user_registered' in dicti:
        dicti.update({'reserva':get_all(request)})
    modificar = request.POST.get('modificar',None)
    borrar = request.POST.get('borrar', None)
    consultar = request.POST.get('consultar', None)
    cargar = request.POST.get('cargar', None)
    crear = request.POST.get('crear', None)
    reservar = request.POST.get('reservar', None)
    user=''
    if 'admin' in dicti:
        user = User.objects.get(username=request.user)
    if 'user_registered' in dicti:
        user = User.objects.get(username=request.user)
    logger.debug(text)
    logger.debug(key)
    logger.debug(crear)
    logger.debug(cargar)
    logger.debug(borrar)
    logger.debug(modificar)
    logger.debug(consultar)
    logger.debug(reservar)
    response_data = {}
    logger.debug(request.POST)
    logger.debug(request.method == 'POST')
    logger.debug(request.is_ajax())
    if request.method == 'POST' and request.is_ajax():
        logger.debug('POST ajax')
        if reservar is not None:
            logger.debug('reservar')
            response_data = reserve(request)
            return JsonResponse(response_data)
        if borrar is not None:
            logger.debug('borrar')
            if text == 'court':
                response_data = delete(request, key, Court)
            if text == 'reservation':
                response_data = delete(request, key, Reservation)
            return JsonResponse(response_data)
        if consultar is not None:
            logger.debug('consultar')
            if text == 'court':
                response_data = retrieve(request, Court, key)
            if text == 'reservation':
                response_data = retrieve(request, Reservation, key)
            return JsonResponse(response_data)
        if modificar is not None:
            logger.debug('modificar')
            if text == 'court':
                response_data = change(request, Court, 'update', 'court')
            if text == 'reservation':
                response_data = change(request, Reservation, 'update', 'reservation')
            return JsonResponse(response_data)  
        if crear is not None:
            logger.debug('crear')
            if text == 'court':
                response_data = create(request, Court, 'create', text)
            if text == 'reservation':
                response_data = create(request, Reservation, 'create', text)
            return JsonResponse(response_data) 
        if cargar is not None:
            logger.debug('cargar')
            if text == 'court':
                response_data = edit(request, key, Court)
                response_data=retrieve(request, Court, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'reservation':
                response_data = edit(request, key, Reservation)
                response_data=retrieve(request, Reservation, key)
                response_data=get_data_dict_reverse(response_data)
            return JsonResponse(response_data)  
    else:
        logger.debug('no POST')
        form_courts = CourtForm()
        form_reservations = ReservationForm()
        form_reserve = ReservateForm()
        dicti.update(csrf(request))
        dicti.update({'form_courts':form_courts, 'form_reservations':form_reservations,
                      'form_reservate':form_reserve,'user':user})
    return render_to_response('court/all_court.html', dicti)
    
def reserve(request):
    form = ReservateForm(request.POST or None, request.FILES or None)
    pk = request.POST.get('court')
    user = request.POST.get('user')
    logger.debug(user)
    court=Court.objects.get(pk=int(pk))
    logger.debug(court)
    logger.debug(form)
    if form.is_valid():
        diccionario=check_reservation(request)
        if bool(diccionario):
            return diccionario
        else:
            form = form.save(commit=False)
            logger.debug('valid')
            duration = request.POST.get('duration', None)
            dura = str(duration).split(':')
            logger.debug(dura)
            form.user = request.user 
            cost = court.price * int(dura[0])
            form.cost=cost
            form.court=court
            form.save()
            data = get_data(request)
            return data
    else:
        logger.debug('invalid')
        response_data = get_error(form)
        return response_data

def upload_file(request):
    """Handle the uploads of file in the system.
    :param request: A Request instance.
    :return: true
    """
    path = '/var/www/pictures/%s' % id
    f = request.FILES['image']
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return True

def check_reservation(request):
    pk = request.POST.get('court')
    duration_to_be = request.POST.get('duration')
    hour_to_be = request.POST.get('hour')
    date = request.POST.get('date')
    court=Court.objects.get(pk=int(pk))
    reservations_hour = Reservation.objects.filter(court=court).filter(date=date)
    logger.debug(reservations_hour)
    dicti={}
    for reservation in reservations_hour:
        hour_reserved = reservation.hour
        duration_reserved = reservation.duration
        if not (check_hour(hour_reserved, duration_reserved, hour_to_be, duration_to_be)):
            dicti.update({'hay_error':True,'Tramo':'La pista esta ocupada en ese tramo.'})
    logger.debug(dicti)
    return dicti
    
def check_hour(hour_reserved, duration_reserved, hour_to_be, duration_to_be):
    hour_reserved = int(str(hour_reserved).split(':')[0])
    hour_to_be = int(str(hour_to_be).split(':')[0])
    logger.debug(hour_reserved)
    logger.debug(hour_to_be)
    duration_reserved = int(str(duration_reserved).split(':')[0])
    duration_to_be = int(str(duration_to_be).split(':')[0])
    logger.debug(duration_reserved)
    logger.debug(duration_to_be)
    if (hour_reserved > hour_to_be) and (hour_reserved<(hour_to_be+duration_to_be)):
        return True
    if (hour_reserved< hour_to_be) and ((hour_reserved+duration_reserved)>hour_to_be):
        return True
    return False