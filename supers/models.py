from django.db import models
#from super_types.models import Super_types

# Create your models here.
class Super(models.Model):
    name = models.CharField(max_length=200)
    alter_ego = models.CharField(max_length=200)
    primary_ability = models.CharField(max_length=200)
    secondary_ability = models.CharField(max_length=200)
    catch_phrase = models.CharField(max_length=200)
    super_type = models.ForeignKey(Super_types, on_delete= models.CASCADE, null=True)