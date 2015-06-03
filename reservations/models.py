from __future__ import unicode_literals

from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def __unicode__( self ):
        return self.name

    class Meta:
        managed = False
        db_table = 'products'

class ProductOption(models.Model):
    product = models.ForeignKey(Product, to_field='id')
    name = models.CharField(max_length=255)
    reserved = models.IntegerField()
    available = models.IntegerField()
    purchased = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()

    def _get_option(self):
        return self.product.name + ' - ' + self.name

    def __unicode__( self ):
        return self.product.name + ' - ' + self.name

    class Meta:
        managed = False
        db_table = 'products_options'
        verbose_name = "Plan"
        verbose_name_plural = "Plans"


class Reservation(models.Model):
    product = models.ForeignKey(Product, to_field='id')
    product_option = models.ForeignKey(ProductOption, to_field='id')
    name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    company = models.CharField(max_length=255)
    role = models.CharField(max_length=255)
    terms = models.IntegerField()
    status = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    transaction_id = models.CharField(max_length=255)
    payer_id = models.CharField(max_length=255)
    completed_at = models.DateTimeField(blank=True, null=True)

    def __unicode__( self ):
        return self.name + 'in ' + self.product.name + ' - ' + self.product_option.name

    class Meta:
        managed = False
        db_table = 'reservations'

class Book(models.Model):
    title = models.CharField(max_length=250)
    status = models.CharField(max_length=250)

    class Meta:
        managed = False
        db_table = 'books'
