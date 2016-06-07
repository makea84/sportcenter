from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .forms import MachineForm, ExerciseForm, ProgrammForm, PlanificationForm, PlanForm
from .models import Machine, Exercise, Programm, Planification

from utils.auxiliar import delete, edit, get_error, get_data, get_data_reverse, get_data_dict,\
    get_data_dict_reverse, check_user, getAllObjects
    
from utils.create_pdf import render_to_pdf

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
        if texto == 'machine':
            form = MachineForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'exercise':
            form = ExerciseForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'programm':
            form = ProgrammForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'planification':
            form = PlanificationForm(request.POST or None, request.FILES or None, instance=instance)
    if operation == 'create':
        if texto == 'machine':
            form = MachineForm(request.POST or None, request.FILES or None)
        if texto == 'exercise':
            form = ExerciseForm(request.POST or None, request.FILES or None)
        if texto == 'programm':
            form = ProgrammForm(request.POST or None, request.FILES or None)
        if texto == 'planification':
            form = PlanificationForm(request.POST or None, request.FILES or None)
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
    if (text is Machine) or (text is Exercise):
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
    data = getAllObjects(Machine, request)
    dictionary={'maquina':data}
    data = getAllObjects(Planification, request)
    dictionary.update({'planificacion':data})
    return render(request,"machine/prueba.html", dictionary)

def get_machine(request):
    """Load machine data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Machine, request)
    dictionary={'maquina':data}
    return render(request,"machine/admin/prueba_maquina.html", dictionary)

def get_exercise(request):
    """Load exercise data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Exercise, request)
    dictionary={'ejercicio':data}
    return render(request,"machine/admin/prueba_ejercicio.html", dictionary)

def get_planification(request):
    """Load planification data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Planification, request)
    dictionary={'planificacion':data}
    return render(request,"machine/admin/prueba_planificacion.html", dictionary)

def get_programm(request):
    """Load programm data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Programm, request)
    dictionary={'programa':data}
    return render(request,"machine/admin/prueba_programa.html", dictionary)

def get_exercise_form(request):
    """Reload exercise form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_exercises = ExerciseForm()
    dictionary = {'form_exercises':form_exercises}
    return render(request,"machine/admin/load_exercise.html", dictionary)

def get_programm_form(request):
    """Reload programm form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_programms = ProgrammForm()
    dictionary = {'form_programms':form_programms}
    return render(request,"machine/admin/load_programm.html", dictionary)

def get_planification_form(request):
    """Reload planification form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_planifications = PlanificationForm()
    dictionary = {'form_planifications':form_planifications}
    return render(request,"machine/admin/load_planification.html", dictionary)

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
        if tipe is Machine:
            obj = tipe.objects.create(**data_reverse)
            obj.save()
            logger.debug(obj)
        if tipe is Exercise:
            data_reverse['image'] = form.cleaned_data['image']
            data_reverse['machine'] = Machine.objects.get(pk=int(data_reverse['machine']))
            obj = tipe.objects.create(**data_reverse)
            obj.save()
            logger.debug(obj)
        if tipe is Programm:
            data_reverse['exercise'] = Exercise.objects.get(pk=int(data_reverse['exercise']))
            obj = tipe.objects.create(**data_reverse)
            obj.save()
            logger.debug(obj)
        if tipe is Planification:
            data_reverse['programm'] = Programm.objects.get(pk=int(data_reverse['programm']))
            obj = tipe.objects.create(**data_reverse)
            obj.save()
        logger.debug('Fin_create')
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

def allMachines(request):
    """Process the view for machine and call other functions and methods
    :param request: A Request instance.
    """
    dicti=check_user(request)
    logger.debug(dicti)
    key = request.POST.get('pk', None)
    text = request.POST.get('tipe', None)
    dicti.update({'maquina':getAllObjects(Machine, request)})
    dicti.update({'ejercicio':getAllObjects(Exercise, request)})
    dicti.update({'programa':getAllObjects(Programm, request)})
    dicti.update({'planificacion':getAllObjects(Planification, request)})
    modificar = request.POST.get('modificar',None)
    borrar = request.POST.get('borrar', None)
    consultar = request.POST.get('consultar', None)
    cargar = request.POST.get('cargar', None)
    crear = request.POST.get('crear', None)
    descargar = request.POST.get('descargar', None)
    adicionar = request.POST.get('adicionar', None)
    quitar = request.POST.get('quitar', None)
    logger.debug(text)
    logger.debug(crear)
    logger.debug(cargar)
    logger.debug(borrar)
    logger.debug(modificar)
    logger.debug(consultar)
    logger.debug(descargar)
    logger.debug(adicionar)
    logger.debug(quitar)
    response_data = {}
    logger.debug(request.POST)
    logger.debug(request.method == 'POST')
    logger.debug(request.is_ajax())
    if request.method == 'POST' and request.is_ajax():
        logger.debug('POST ajax')
        if adicionar is not None:
            response_data = adicionar_programa(request,text)
            return JsonResponse(response_data)
        if quitar is not None:
            response_data = quitar_programa(request,text)
            return JsonResponse(response_data)
        if descargar is not None:
            response_data = getPDF(request)
            return response_data
        if borrar is not None:
            logger.debug('borrar')
            if text == 'machine':
                response_data = delete(request, key, Machine)
            if text == 'exercise':
                response_data = delete(request, key, Exercise)
            if text == 'planification':
                response_data = delete(request, key, Planification)
            if text == 'programm':
                response_data = delete(request, key, Programm)
            return JsonResponse(response_data)
        if consultar is not None:
            logger.debug('consultar')
            if text == 'machine':
                response_data = retrieve(request, Machine, key)
            if text == 'exercise':
                response_data = retrieve(request, Exercise, key)
            if text == 'planification':
                response_data = retrieve(request, Planification, key)
            if text == 'programm':
                response_data = retrieve(request, Programm, key)
            return JsonResponse(response_data)
        if modificar is not None:
            logger.debug('modificar')
            if text == 'machine':
                response_data = change(request, Machine, 'update', 'machine')
            if text == 'exercise':
                response_data = change(request, Exercise, 'update', 'exercise')
            if text == 'planification':
                response_data = change(request, Planification, 'update', 'planification')
            if text == 'programm':
                response_data = change(request, Programm, 'update', 'programm')
            return JsonResponse(response_data)  
        if crear is not None:
            logger.debug('crear')
            if text == 'machine':
                response_data = create(request, Machine, 'create', text)
            if text == 'exercise':
                response_data = create(request, Exercise, 'create', text)
            if text == 'planification':
                response_data = create(request, Planification, 'create', text)
            if text == 'programm':
                response_data = create(request, Programm, 'create', text)
            return JsonResponse(response_data) 
        if cargar is not None:
            logger.debug('cargar')
            if text == 'machine':
                response_data = edit(request, key, Machine)
                response_data=retrieve(request, Machine, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'exercise':
                response_data = edit(request, key, Exercise)
                response_data=retrieve(request, Exercise, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'planification':
                response_data = edit(request, key, Planification)
                response_data=retrieve(request, Planification, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'programm':
                response_data = edit(request, key, Programm)
                response_data=retrieve(request, Programm, key)
                response_data=get_data_dict_reverse(response_data)
            return JsonResponse(response_data)  
    else:
        logger.debug('no POST')
        form_machines = MachineForm()
        form_exercises = ExerciseForm()
        form_programms = ProgrammForm()
        form_planifications = PlanificationForm()
        form_plan = PlanForm()
        dicti.update(csrf(request))
        dicti.update({'form_machines':form_machines, 'form_exercises':form_exercises,
             'form_programms':form_programms, 'form_planifications':form_planifications,
             'form_plan':form_plan,})
    return render_to_response('machine/all_machine.html', dicti)

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

def getPDF(request):
    pk = request.POST.get('pk', None)
    dicti={}
    planifications = Planification.objects.prefetch_related('programm').all().filter(pk=pk)
    data = set()
    for programm in Programm.objects.all():
        if planifications.filter(programm=programm).exists():
            data.add(programm.pk)
    data = Programm.objects.filter(pk__in=data)
    dicti.update({'programms':data})
    planifications = zip(planifications)
    logger.debug(planifications)
    exercises = Exercise.objects.prefetch_related('machine').all()
    exercises = zip(exercises)
    dicti.update({'exercises':exercises})
    dicti.update({'pagesize':'A4'})
    dicti.update({'planifications':planifications})
    return render_to_pdf('machine/pdf_template.html',dicti)


def example(request):
    exercises = Exercise.objects.all().select_related('machine')
    exercises = zip(exercises)
    dicti={'exercises':exercises}
    return render_to_response('machine/prueba.html', dicti)

def adicionar_programa(request,text):
    pk = request.POST.get('planification')
    programm = request.POST.get('programm')
    logger.debug(programm)
    plan=Planification.objects.get(pk=int(pk))
    logger.debug(dir(plan))
    progr = Programm.objects.get(pk=int(programm))
    logger.debug(dir(progr))
    logger.debug(programm)
    logger.debug(plan)
    progr.planification_programm.add(plan)
    data = {'Adicionar':'Se ha adicionado el programa.'}
    return data

def quitar_programa(request, text):
    form = PlanForm(request.POST or None, request.FILES or None)
    pk = request.POST.get('planification')
    programm = request.POST.get('programm')
    plan=Planification.objects.get(pk=int(pk))
    progr = Programm.objects.get(pk=int(programm))
    logger.debug(form)
    progr.planification_programm.remove(plan)
    data = {'Quitar':'Se ha quitado el programa.'}
    return data
