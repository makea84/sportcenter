from django.db import models
from django.core.validators import RegexValidator

class Product(models.Model):
    """Represents a Product existing in the gym.
    :idProduct: The primary key for the product.
    :name: The name for the product. Must be unique.
    :description: More information about the product.
    :image: A image of the product.
    :price: The price of the product.
    """
    idProduct = models.AutoField(
        primary_key=True,
        verbose_name='Producto',
        db_column='idProduct',
    )
    name = models.CharField(
        max_length=200,
        unique=True, default='',
        verbose_name='Nombre',
        db_column='name',
        help_text='Solo letras, numeros y espacios.',
        validators=[
            RegexValidator(
                regex='^([0-9a-zA-Z][, .:]*){1,200}$',
                message='Solo letras, puntuacion y numeros, maximo 200.', 
                code='invalid_name',
            )
        ],
    )
    description = models.TextField(
        verbose_name='Descripcion',
        db_column='description',
        help_text='Solo letras, numeros y espacios.',
        default='',
        validators=[
            RegexValidator(
                regex='^([0-9a-zA-Z][, .:]*){1,500}$',
                message='Solo letras, puntuacion y numeros, maximoa 500.', 
                code='invalid_description',
            )
        ],
    )
    image = models.ImageField(
        upload_to='product/',
        verbose_name='Imagen',
        db_column='image',
        help_text='jpg,bmp,svg o png.',
    )
    price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name='Precio',
        db_column='price',
        help_text='1 a 3 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,3}\.[0-9]{1,2})|([0-9]{1,3}))$',
                message='1 a 3 parte entera y 2 parte decimal.', 
                code='invalid_price',
            )
        ],
    )

    class Meta:
        db_table = 'Product'
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

    def __unicode__(self):
        return self.name


class Stock(models.Model):
    """Represents the Stock of a existing product.
    :idStock: The primary key for the stock.
    :product: The product which the stock referes. FK for Product.
    :quantity: The number of this product existing in the gym.
    """
    idStock = models.AutoField(
        primary_key=True,
        verbose_name='Stock',
        db_column='idStock',
    )
    product = models.ForeignKey(
        Product,
        related_name='stock_product',
        verbose_name='Producto',
        db_column='product',
    )
    quantity = models.CharField(
        max_length=2, 
        verbose_name='Cantidad', 
        db_column='quantity',
        help_text='Minimo 1, maximo 99.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]{1,1}|[1-9]{1,1}[0-9]{1,1})$',
                message='Entre 1 y 99.', 
                code='invalid_quantity',
            )
        ],
    )

    class Meta:
        db_table = 'Stock'
        verbose_name = 'Stock'
        verbose_name_plural = 'Stocks'

    def __unicode__(self):
        return self.product.name + '->' + self.quantity


class Line(models.Model):
    """Represents the Line of a product in a bill.
    :idLine: The primary key for the line.
    :product: The product which the line referes. FK for Product.
    :price: The price of the product in the line.
    :quantity: The number of this product existing in the line.
    :subtotal: The subtotal of the line. price x quantity.
    """
    idLine = models.AutoField(
        primary_key=True,
        verbose_name='Linea',
        db_column='idLine',
    )
    product = models.ForeignKey(
        Product,
        related_name='line_product',
        verbose_name='Producto',
        db_column='product',
    )
    price = models.DecimalField(
        max_digits=7,
        decimal_places=2,
        verbose_name='Precio',
        db_column='price',
        help_text='1 a 5 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,5}\.[0-9]{1,2})|([0-9]{1,5}))$',
                message='1 a 5 parte entera y 2 parte decimal.', 
                code='invalid_price',
            )
        ],
    )
    quantity = models.CharField(
        max_length=2, 
        verbose_name='Cantidad', 
        db_column='quantity',
        help_text='Minimo 1, maximo 99.', 
        default=1,
        validators=[
            RegexValidator(
                regex='^([1-9]{1,1}|[1-9]{1,1}[0-9]{1,1})$',
                message='Entre 1 y 99.', 
                code='invalid_quantity',
            )
        ],
    )
    subtotal = models.DecimalField(
        max_digits=8,
        decimal_places=2,
        verbose_name='Subtotal',
        db_column='subtotal',
        help_text='1 a 6 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,6}\.[0-9]{1,2})|([0-9]{1,6}))$',
                message='1 a 6 parte entera y 2 parte decimal.', 
                code='invalid_subtotal',
            )
        ],
    )

    class Meta:
        db_table = 'Line'
        verbose_name = 'Linea'
        verbose_name_plural = 'Lineas'

    def __unicode__(self):
        return str(self.idLine)


class Bill(models.Model):
    """Represents the Bill of a sale.
    :idBill: The primary key for the bill.
    :line: A line inside the bill. FK for Line.
    :total: The total of the bill.
    :date: The date when the bill is created.
    """
    idBill = models.AutoField(
        primary_key=True,
        verbose_name='Factura',
        db_column='idBill',
    )
    line = models.ForeignKey(
        Line,
        related_name='bill_line',
        verbose_name='Linea',
        db_column='line',
    )
    total = models.DecimalField(
        max_digits=9,
        decimal_places=2,
        verbose_name='Total',
        db_column='total',
        help_text='1 a 7 parte entera, 2 parte decimal.',
        default=0.0,
        validators=[
            RegexValidator(
                regex='^(([0-9]{1,7}\.[0-9]{1,2})|([0-9]{1,7}))$',
                message='1 a 7 parte entera y 2 parte decimal.', 
                code='invalid_total',
            )
        ],
    )
    date = models.CharField(
        verbose_name='Fecha',
        db_column='date',
        help_text='aaaa-mm-dd.',
        default='2016-06-10',
        max_length=10,
        validators=[
            RegexValidator(
                regex='^([2-9][0-9]{3})\-(0[1-9]|1[0-2])\-(0[1-9]|[1|2][0-9]|[3][0|1])$',
                message='aaaa-mm-dd.', 
                code='invalid_date',
            )
        ],
    )

    class Meta:
        db_table = 'Bill'
        verbose_name = 'Factura'
        verbose_name_plural = 'Facturas'

    def __unicode__(self):
        return str(self.idBill)
