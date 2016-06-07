#!/usr/bin/env python
# -*- coding: utf-8 -*-
import logging
from django.forms.models import model_to_dict
import collections
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

logger = logging.getLogger('sportcenter.page_processors')


DICT_LABELS = {'image':'Imagen','name':'Nombre', 'description':'Descripcion', 
               'price':'Precio','cost':'Coste','date':'Fecha',
               'hour':'Hora','duration':'Duracion','total':'Total',
               'subtotal':'Subtotal','avaible':'Disponible','quantity':'Cantidad',
               'capacity':'Capacidad','width':'Ancho','length':'Largo',
               'series':'Series','rest':'Descanso',
               'day':'Dia','user':'Usuario','court':'Pista',
               'classroom':'Clase','course':'Curso','product':'Producto',
               'machine':'Maquina','exercise':'Ejercicio','programm':'Programa',
               'zone':'Zona','line':'Linea','stock':'Stock'}


DICT_LABELS_REVERSE = {'Imagen':'image','Nombre':'name', 'Descripcion':'description', 
               'Precio':'price','Coste':'cost','Fecha':'date',
               'Hora':'hour','Duracion':'duration','Total':'total',
               'Subtotal':'subtotal','Disponible':'avaible','Cantidad':'quantity',
               'Capacidad':'capacity','Ancho':'width','Largo':'length',
               'Series':'series','Descanso':'rest',
               'Dia':'day','Usuario':'user','Pista':'court',
               'Clase':'classroom','Curso':'course','Producto':'product',
               'Maquina':'machine','Ejercicio':'exercise','Programa':'programm',
               'Zona':'zone','Linea':'line','Stock':'stock'}

def getAllObjects(text, request):
    """Get all objects of a type, and set a paginator for it
    :param request: A Request instance.
    :param text: Type of the element
    :type text: Object type
    :return: queryset and paginator
    """
    data = text.objects.all()
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
    
def get_data_dict(diccionario):
    """Return a dict with key-value of a element in the system.
    :param diccionario: dictionary with key-value of element
    :return: dictionary with key changed
    """
    logger.debug('get data')
    diccionario = collections.OrderedDict(diccionario)
    dictionary = collections.OrderedDict()
    for key, value in diccionario.items():
        if key in DICT_LABELS:
            dictionary.update({DICT_LABELS[key]:value})
    logger.debug(dictionary)
    return dictionary

def get_data_dict_reverse(diccionario):
    """Return a dict with key-value of a element in the system.
    :param diccionario: dictionary with key-value of element
    :return: dictionary with keys changed
    """
    logger.debug('get data')
    diccionario = collections.OrderedDict(diccionario)
    dictionary = collections.OrderedDict()
    for key, value in diccionario.items():
        if key in DICT_LABELS_REVERSE:
            dictionary.update({DICT_LABELS_REVERSE[key]:value})
    logger.debug(dictionary)
    return dictionary

def delete(request, pk, text):
    """Delete a element in the system.
    :param pk: Primary key of the element to be delete.
    :type pk: int
    :param text: Type of the element to be delete.
    :type text: obj
    :param request: A Request instance.
    :return: dictionary with the element state
    """
    diccionario = {}
    query = text.objects.get(pk=pk)
    logger.debug('delete')
    diccionario.update(model_to_dict(query , exclude='image'))
    query.delete()
    return get_data_dict(diccionario)

def edit(request, pk, text):
    """Return a element match with pk and text in the system.
    :pk: Primary key of the element.
    :type pk: int
    :text: Type of the element.
    :type text: obj
    :param request: A Request instance.
    :return: matched element in dict format
    """
    query = text.objects.get(pk=int(pk))
    logger.debug('edit')
    logger.debug(model_to_dict(query))
    return model_to_dict(query)

def get_error(form):
    """Get the errors of a form.
    :form: Form to check errors.
    :type form: form
    :return: dictionary with the errors
    """
    logger.debug('get error')
    diccionario = {}
    error = form.errors
    logger.debug(error)
    for field in form:
        if bool(form[field.name].errors):
            labels = field.label.decode('utf8')
            logger.debug(labels)
            diccionario.update({labels.encode('utf8'):form[field.name].errors})
    diccionario.update({'hay_error':True})
    logger.debug(diccionario)
    return diccionario

def get_data(request):
    """Return a dict with key-value of a element in the system.
    :param request: A Request instance.
    :return: dictionary with the data
    """
    logger.debug('get data')
    dictionary = {}
    for field in request.POST:
        if field in DICT_LABELS:
            dicti={DICT_LABELS[field]:request.POST[field]}
            dictionary.update(dicti)
    for field in request.FILES:
        if field in DICT_LABELS:
            dictionary.update({DICT_LABELS[field]:request.FILES[field]})
    logger.debug(request.POST)
    logger.debug(dictionary)
    return dictionary

def get_data_reverse(dicti):
    """Return a dict with key-value of a element in the system.
    :param dicti: dictionary with the data of element
    :type dicti: dict
    :return: dictionary with the key changed
    """
    logger.debug('get data reverse')
    dictionary = {}
    for key in dicti:
        if key in DICT_LABELS_REVERSE:
            dictionary.update({DICT_LABELS_REVERSE[key]:dicti[key]})
    logger.debug(dictionary)
    return dictionary

def get_related_element(text, obj):
    """Return a dict with key-value of a element in the system.
    :param text: type of the element
    :type text: Object type
    :param obj: Primary key of the element
    :type obj: int
    :return: dict with the data of the element
    """
    element = text.objects.get(pk=obj)
    return model_to_dict(element)

def check_user(request):
    """Return a dict with key-value of user connected.
    :param request: A Request instance.
    :return: dict
    """
    diccionario={}
    if request.user.is_superuser:
        diccionario.update({'admin':'si'})
        return diccionario
    if request.user.is_authenticated():
        diccionario.update({'user_registered':'si'})
        return diccionario
    diccionario.update({'user_unregistered':'si'})
    logger.debug(diccionario)
    return diccionario

def upload_file(request):
    path = '/var/www/pictures/%s' % id
    f = request.FILES['image']
    destination = open(path, 'wb+')
    for chunk in f.chunks():
        destination.write(chunk)
    destination.close()
    return True    