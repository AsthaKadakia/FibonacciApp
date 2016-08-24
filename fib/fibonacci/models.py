from __future__ import unicode_literals

from django.db import models

# Create your models here.


class FibonacciParameters(models.Model):
    type_id = models.IntegerField()
    exec_time = models.DecimalField(decimal_places=10,max_digits=1000)
    input_parameter = models.CharField(max_length=100000)
    result = models.CharField(max_length=100000)

