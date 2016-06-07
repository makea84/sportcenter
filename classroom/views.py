from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.forms.models import model_to_dict
from django.contrib.auth.models import User
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

from .forms import ClassroomForm, CourseForm, PlaceForm, ParticipationForm
from .models import Classroom, Course, Place, Participation

from utils.auxiliar import delete, edit, get_error, get_data, get_data_reverse, get_data_dict,\
    get_data_dict_reverse, check_user, getAllObjects

import logging
import collections

logger = logging.getLogger('sportcenter.page_processors')

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
        if texto == 'course':
            form = CourseForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'classroom':
            form = ClassroomForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'place':
            form = PlaceForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'participation':
            form = ParticipationForm(request.POST or None, request.FILES or None, instance=instance)
    if operation == 'create':
        if texto == 'course':
            form = CourseForm(request.POST or None, request.FILES or None)
        if texto == 'classroom':
            form = ClassroomForm(request.POST or None, request.FILES or None)
        if texto == 'place':
            form = PlaceForm(request.POST or None, request.FILES or None)
        if texto == 'participation':
            form = ParticipationForm(request.POST or None, request.FILES or None)
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
    logger.debug('retrieve')
    obj = text.objects.get(pk=pk)
    if text is Classroom:
        imagen = obj.image.path.split('/')
        imagen = imagen[len(imagen)-2]+'/'+imagen[len(imagen)-1]
        diccion = {'image':imagen}
        dicti = collections.OrderedDict(diccion)
        dicti.update(model_to_dict(obj, exclude=['image']))
        return get_data_dict(dicti)
    return get_data_dict(model_to_dict(obj))

def get_other_user(request):
    """Load data for user template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Classroom, request)
    dictionary={'clase':data}
    data = getAllObjects(Course, request)
    dictionary.update({'curso':data})
    return render(request,"classroom/prueba.html", dictionary)

def get_classroom(request):
    """Load classroom data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Classroom, request)
    dictionary={'clase':data}
    return render(request,"classroom/admin/prueba_clase.html", dictionary)

def get_course(request):
    """Load course data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Course, request)
    dictionary={'curso':data}
    return render(request,"classroom/admin/prueba_curso.html", dictionary)

def get_my_course(request):
    """Load course data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = mi_curso(request)
    dictionary={'mi_curso':data}
    return render(request,"classroom/user/prueba_curso_2.html", dictionary)

def get_no_my_course(request):
    """Load course data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = no_curso(request)
    dictionary={'no_curso':data}
    return render(request,"classroom/user/prueba_curso.html", dictionary)

def get_participation(request):
    """Load participation data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Participation, request)
    dictionary={'participacion':data}
    return render(request,"classroom/admin/prueba_participacion.html", dictionary)

def get_place(request):
    """Load place data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Place, request)
    dictionary={'lugar':data}
    return render(request,"classroom/admin/prueba_lugar.html", dictionary)

def get_participation_form(request):
    """Reload participation form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_participations = ParticipationForm()
    dictionary = {'form_participations':form_participations}
    return render(request,"classroom/admin/load_participation.html", dictionary)

def get_place_form(request):
    """Reload place form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_places = PlaceForm()
    dictionary = {'form_places':form_places}
    return render(request,"classroom/admin/load_place.html", dictionary)

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
        if tipe is Classroom:
            data_reverse['image'] = form.cleaned_data['image']
        if tipe is Place:
            classroom = data_reverse['classroom']
            data_reverse['classroom'] = Classroom.objects.get(pk=classroom)
            course = data_reverse['course']
            data_reverse['course'] = Course.objects.get(pk=course)
        if tipe is Participation:
            course = data_reverse['course']
            data_reverse['course'] = Course.objects.get(pk=course)
            user = data_reverse['user']
            data_reverse['user'] = User.objects.get(pk=user)
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
    logger.debug('change')
    form = select_operation(request, text, operation, texto)
    if form.is_valid():
        logger.debug('valid')
        form.save()
        data = get_data(request)
        return data
    else:
        logger.debug('invalid')
        response_data = get_error(form)
        return response_data

def allClassrooms(request):
    """Process the view for classroom and call other functions and methods
    :param request: A Request instance.
    """
    dicti=check_user(request)
    logger.debug(dicti)
    key = request.POST.get('pk', None)
    text = request.POST.get('tipe', None)
    dicti.update({'clase':getAllObjects(Classroom, request)})
    if 'admin' in dicti:
        dicti.update({'curso':getAllObjects(Course, request)})
    if 'user_unregistered' in dicti:
        dicti.update({'curso':getAllObjects(Course, request)})
    if 'user_registered' in dicti:
        dicti.update({'no_curso':no_curso(request)})
        dicti.update({'mi_curso':mi_curso(request)})
    dicti.update({'lugar':getAllObjects(Place, request)})
    dicti.update({'participacion':getAllObjects(Participation, request)})
    modificar = request.POST.get('modificar',None)
    borrar = request.POST.get('borrar', None)
    consultar = request.POST.get('consultar', None)
    cargar = request.POST.get('cargar', None)
    crear = request.POST.get('crear', None)
    apuntar = request.POST.get('apuntar', None)
    desapuntar = request.POST.get('desapuntar', None)
    logger.debug(text)
    logger.debug(crear)
    logger.debug(cargar)
    logger.debug(borrar)
    logger.debug(modificar)
    logger.debug(consultar)
    response_data = {}
    logger.debug(request.POST)
    logger.debug(request.method == 'POST')
    logger.debug(request.is_ajax())
    if request.method == 'POST' and request.is_ajax():
        logger.debug('POST ajax')
        if apuntar is not None:
            logger.debug('apuntar')
            response_data = join_in(request, key)
            return JsonResponse(response_data)
        if desapuntar is not None:
            logger.debug('desapuntar')
            response_data = disjoin_in(request, key)
            return JsonResponse(response_data)
        if borrar is not None:
            logger.debug('borrar')
            if text == 'course':
                response_data = delete(request, key, Course)
            if text == 'classroom':
                response_data = delete(request, key, Classroom)
            if text == 'participation':
                response_data = delete(request, key, Participation)
            if text == 'place':
                response_data = delete(request, key, Place)
            return JsonResponse(response_data)
        if consultar is not None:
            logger.debug('consultar')
            if text == 'course':
                response_data = retrieve(request, Course, key)
            if text == 'classroom':
                response_data = retrieve(request, Classroom, key)
            if text == 'participation':
                response_data = retrieve(request, Participation, key)
            if text == 'place':
                response_data = retrieve(request, Place, key)
            return JsonResponse(response_data)
        if modificar is not None:
            logger.debug('modificar')
            if text == 'course':
                response_data = change(request, Course, 'update', 'course')
            if text == 'classroom':
                response_data = change(request, Classroom, 'update', 'classroom')
            if text == 'participation':
                response_data = change(request, Participation, 'update', 'participation')
            if text == 'place':
                response_data = change(request, Place, 'update', 'place')
            return JsonResponse(response_data)  
        if crear is not None:
            logger.debug('crear')
            if text == 'course':
                response_data = create(request, Course, 'create', text)
            if text == 'classroom':
                response_data = create(request, Classroom, 'create', text)
            if text == 'participation':
                response_data = create(request, Participation, 'create', text)
            if text == 'place':
                response_data = create(request, Place, 'create', text)
            return JsonResponse(response_data) 
        if cargar is not None:
            logger.debug('cargar')
            if text == 'course':
                response_data = edit(request, key, Course)
                response_data=retrieve(request, Course, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'classroom':
                response_data = edit(request, key, Classroom)
                response_data=retrieve(request, Classroom, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'participation':
                response_data = edit(request, key, Participation)
                response_data=retrieve(request, Participation, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'place':
                response_data = edit(request, key, Place)
                response_data=retrieve(request, Place, key)
                response_data=get_data_dict_reverse(response_data)
            return JsonResponse(response_data)
    else:
        logger.debug('no POST')
        form_courses = CourseForm()
        form_classrooms = ClassroomForm()
        form_places = PlaceForm()
        form_participations = ParticipationForm()
        dicti.update(csrf(request))
        dicti.update({'form_courses': form_courses, 'form_classrooms': form_classrooms,
             'form_places': form_places, 'form_participations': form_participations})
    return render_to_response('classroom/all_classroom.html', dicti)

def join_in(request,pk):
    course=Course.objects.get(pk=int(pk))
    user=request.user
    Participation.objects.create(course=course,user=user)
    dicti = {}
    dicti.update({'Apuntado':'Se ha apuntado al curso'})
    return dicti

def disjoin_in(request,pk):
    course=Course.objects.get(pk=int(pk))
    user=User.objects.get(username=request.user)
    logger.debug(course)
    logger.debug(user)
    participacion=Participation.objects.get(user=user, course=course)
    participacion.delete()
    dicti = {}
    dicti.update({'Desapuntado':'Se ha desapuntado del curso'})
    return dicti

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

def no_curso(request):
    courses = Course.objects.all()
    data = set()
    for course in courses:
        if not (Participation.objects.filter(user=request.user).filter(course=course).exists()):
            data.add(course.pk)
    data = Course.objects.filter(pk__in = data)
    paginator = Paginator(data, 2)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    no_curso = data
    logger.debug(no_curso)
    return no_curso

def mi_curso(request):
    data = Participation.objects.prefetch_related('course').all().filter(user=request.user)
    paginator = Paginator(data, 2)
    page = request.GET.get('page')
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    mi_curso = data
    logger.debug(mi_curso)
    return mi_curso