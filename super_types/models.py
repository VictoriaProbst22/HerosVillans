from django.db import models
from supers.models import Super
# Create your models here.
class Super_types(models.Model):
    type = models.CharField(max_length=200)
    super_type = models.ForeignKey(Super, on_delete= models.CASCADE, null=True)