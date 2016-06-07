# encoding:utf-8
from django.forms import ModelForm, Textarea, TextInput
from .models import Product, Line, Stock, Bill

class ProductForm(ModelForm):
    """Represents a form for a Product.
    :name: The name for the product. Must be unique.
    :description: Other information of the product.
    :price: The price of the product.
    :image: A image of the product.
    """
    class Meta:
        model = Product
        fields =('name', 'description', 'price', 'image')
        labels ={
            'name':'Nombre', 'description':'Descripcion',
            'price':'Precio', 'image':'Imagen',
        },
        help_texts = {
            'name':'Solo letras, numeros y espacios.',
            'description':'Solo letras, numeros y espacios.',
            'price':'Precio expresado en euros.',    
        },
        error_messages = {
            'name': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 200.',
                'required':'Campo obligatorio.',
            },
            'description': {
                'min_length':'Longitud minima 1.',
                'max_length':'Longitud maxima 500.',
                'required':'Campo obligatorio.',
            },
            'price': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
        },
        widgets = {
            'name': TextInput(attrs={'placeholder': 'Longitud entre 1 y 200.'}),
            'avaible': TextInput(attrs={'placeholder': 'Si o No.'}),
            'description': Textarea(attrs={'placeholder': 'Longitud entre 1 y 500.','rows':'2'}),
            'price': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'999.99',
                            'step':'0.01'
                        }
            ),
        }
        
class StockForm(ModelForm):
    """Represents a form for the Stock of a product.
    :product: The product which the stock referes.
    :quantity: The number of this product avaible in this momment.
    """
    class Meta:
        model = Stock
        fields =('product', 'quantity',)
        labels ={
            'product':'Producto', 'quantity':'Cantidad',
        },
        help_texts = {
            'quantity':'Dos digitos maximo.',    
        },
        error_messages = {
            'quantity': {
                'min_value':'Valor minimo 1.',
                'max_value':'Valor maximo 99.',
                'required':'Campo obligatorio.',
                'invalid':'Cantidad no valida'
            },
        },
        widgets = {
            'quantity': TextInput(
                            attrs={
                                'placeholder': 'Entre 1-99.',
                                'type':'number',
                                'min':'1',
                                'max':'99',
                                'step':'1'
                            }
            ),
        }

class LineForm(ModelForm):
    """Represents a form for a Line in a bill.
    :product: The product which the line referes. FK for Product.
    :price: The price of the product.
    :quantity: The number of this product.
    :subtotal: The subtotal of the line. price x quantity.
    """
    class Meta:
        model = Line
        fields =('product', 'price', 'quantity', 'subtotal',)
        labels ={
            'product':'Producto', 'quantity':'Cantidad', 'subtotal':'Subtotal',
            'price':'Precio',
        },
        help_texts = {
            'price':'Precio expresado en euros.',
            'subtotal':'Subtotal expresado en euros.',
            'quantity':'Dos digitos maximo.',     
        },
        error_messages = {
            'subtotal': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
            'price': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
            'quantity': {
                'min_value':'Valor minimo 1.',
                'max_value':'Valor maximo 99.',
                'required':'Campo obligatorio.',
                'invalid':'Cantidad no valida.'
            },
        },
        widgets = {
            'subtotal': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-99999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'99999.99',
                            'step':'0.01'
                        }
            ),
            'price': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'999.99',
                            'step':'0.01'
                        }
            ),
            'quantity': TextInput(
                            attrs={
                                'placeholder': 'Entre 1-99.',
                                'type':'number',
                                'min':'1',
                                'max':'99',
                                'step':'1'
                            }
            ),
        }

class BillForm(ModelForm):
    """Represents a form for the Bill.
    :line: lines inside the bill. FK for Line.
    :total: The total cost of the bill.
    :date: The date when the bill is created.
    """
    class Meta:
        model = Bill
        fields =('line', 'date', 'total',)
        labels ={
            'line':'Linea', 'date':'Fecha', 'total':'Total',
        },
        help_texts = {
            'date':'Formato dd/mm/aaaa.',
            'total':'Total expresado en euros.',    
        },
        error_messages = {
            'total': {
                'invalid':'Cantidad no permitida.',
                'required':'Campo obligatorio.',
            },
            'date': {
                'invalid':'Fecha no valida.', 
                'required':'Campo obligatorio.'
            },
        },
        widgets = {
            'total': TextInput(
                        attrs={
                            'placeholder': 'Entre 0-99999.99.',
                            'type':'number',
                            'min':'0',
                            'max':'99999.99',
                            'step':'0.01'
                        }
            ),
            'date': TextInput(
                        attrs={
                            'placeholder': 'dd-mm-aaaa.',
                            'type':'date',
                            'min':'2016-06-06'
                        }
            ),
        } 