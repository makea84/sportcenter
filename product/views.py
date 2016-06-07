from django.shortcuts import render_to_response, get_object_or_404, render
from django.template.context_processors import csrf
from django.http import JsonResponse
from django.forms.models import model_to_dict

from .forms import ProductForm, StockForm, LineForm, BillForm
from .models import Product, Stock, Line, Bill

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
        if texto == 'product':
            form = ProductForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'stock':
            form = StockForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'line':
            form = LineForm(request.POST or None, request.FILES or None, instance=instance)
        if texto == 'bill':
            form = BillForm(request.POST or None, request.FILES or None, instance=instance)
    if operation == 'create':
        if texto == 'product':
            form = ProductForm(request.POST or None, request.FILES or None)
        if texto == 'stock':
            form = StockForm(request.POST or None, request.FILES or None)
        if texto == 'line':
            form = LineForm(request.POST or None, request.FILES or None)
        if texto == 'bill':
            form = BillForm(request.POST or None, request.FILES or None)
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
    if text is Product:
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
    data = getAllObjects(Product, request)
    dictionary={'producto':data}
    data = getAllObjects(Stock, request)
    dictionary.update({'stock':data})
    return render(request,"product/prueba.html", dictionary)

def get_product(request):
    """Load product data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Product, request)
    dictionary={'producto':data}
    return render(request,"product/admin/prueba_producto.html", dictionary)

def get_stock(request):
    """Load stock data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Stock, request)
    dictionary={'stock':data}
    return render(request,"product/admin/prueba_stock.html", dictionary)

def get_line(request):
    """Load line data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Line, request)
    dictionary={'linea':data}
    return render(request,"product/admin/prueba_linea.html", dictionary)

def get_bill(request):
    """Load bill data for template.
    :param request: A Request instance.
    :return: html plain text
    """
    data = getAllObjects(Bill, request)
    dictionary={'factura':data}
    return render(request,"product/admin/prueba_factura.html", dictionary)

def get_stock_form(request):
    """Reload stock form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_stocks = StockForm()
    dictionary = {'form_stocks':form_stocks}
    return render(request,"product/admin/load_stock.html", dictionary)

def get_line_form(request):
    """Reload line form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_lines = LineForm()
    dictionary = {'form_lines':form_lines}
    return render(request,"product/admin/load_line.html", dictionary)

def get_bill_form(request):
    """Reload bill form for template.
    :param request: A Request instance.
    :return: html plain text
    """
    form_bills = BillForm()
    dictionary = {'form_bills':form_bills}
    return render(request,"product/admin/load_bill.html", dictionary)

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
        if tipe is Product:
            data_reverse['image'] = form.cleaned_data['image']
        if tipe is Stock:
            product = data_reverse['product']
            data_reverse['product'] = Product.objects.get(pk=product)
        if tipe is Line:
            product = data_reverse['product']
            data_reverse['product'] = Product.objects.get(pk=product)
        if tipe is Bill:
            line = data_reverse['line']
            data_reverse['line'] = Line.objects.get(pk=line)
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

def allProducts(request):
    """Process the view for product and call other functions and methods
    :param request: A Request instance.
    """
    dicti=check_user(request)
    logger.debug(dicti)
    key = request.POST.get('pk', None)
    text = request.POST.get('tipe', None)
    dicti.update({'producto':getAllObjects(Product, request)})
    dicti.update({'stock':getAllObjects(Stock, request)})
    dicti.update({'linea':getAllObjects(Line, request)})
    dicti.update({'factura':getAllObjects(Bill, request)})
    modificar = request.POST.get('modificar',None)
    borrar = request.POST.get('borrar', None)
    consultar = request.POST.get('consultar', None)
    cargar = request.POST.get('cargar', None)
    crear = request.POST.get('crear', None)
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
        if borrar is not None:
            logger.debug('borrar')
            if text == 'product':
                response_data = delete(request, key, Product)
            if text == 'stock':
                response_data = delete(request, key, Stock)
            if text == 'line':
                response_data = delete(request, key, Line)
            if text == 'bill':
                response_data = delete(request, key, Bill)
            return JsonResponse(response_data)
        if consultar is not None:
            logger.debug('consultar')
            if text == 'product':
                response_data = retrieve(request, Product, key)
            if text == 'stock':
                response_data = retrieve(request, Stock, key)
            if text == 'line':
                response_data = retrieve(request, Line, key)
            if text == 'bill':
                response_data = retrieve(request, Bill, key)
            return JsonResponse(response_data)
        if modificar is not None:
            logger.debug('modificar')
            if text == 'product':
                response_data = change(request, Product, 'update', 'product')
            if text == 'stock':
                response_data = change(request, Stock, 'update', 'stock')
            if text == 'line':
                response_data = change(request, Line, 'update', 'line')
            if text == 'bill':
                response_data = change(request, Bill, 'update', 'bill')
            return JsonResponse(response_data)  
        if crear is not None:
            logger.debug('crear')
            if text == 'product':
                response_data = create(request, Product, 'create', text)
            if text == 'stock':
                response_data = create(request, Stock, 'create', text)
            if text == 'line':
                response_data = create(request, Line, 'create', text)
            if text == 'bill':
                response_data = create(request, Bill, 'create', text)
            return JsonResponse(response_data) 
        if cargar is not None:
            logger.debug('cargar')
            if text == 'product':
                response_data = edit(request, key, Product)
                response_data=retrieve(request, Product, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'stock':
                response_data = edit(request, key, Stock)
                response_data=retrieve(request, Stock, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'line':
                response_data = edit(request, key, Line)
                response_data=retrieve(request, Line, key)
                response_data=get_data_dict_reverse(response_data)
            if text == 'bill':
                response_data = edit(request, key, Bill)
                response_data=retrieve(request, Bill, key)
                response_data=get_data_dict_reverse(response_data)
            return JsonResponse(response_data)
    else:
        logger.debug('no POST')
        form_products = ProductForm()
        form_stocks = StockForm()
        form_lines = LineForm()
        form_bills = BillForm()
        dicti.update(csrf(request))
        dicti.update({'form_products': form_products, 'form_stocks': form_stocks,
             'form_lines': form_lines, 'form_bills': form_bills})
    return render_to_response('product/all_product.html', dicti)
    
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