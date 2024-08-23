from django.db import models

# Create your models here.


class Orders(models.Model):
    user_id = models.IntegerField()
    product_id = models.IntegerField()
    total_amount = models.IntegerField()
    
