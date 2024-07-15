from django.db import models
from .validators import is_basic_valid_indian_number

# Create your models here.
class Contact_us(models.Model):
    
    name = models.CharField(max_length=100)
    phone_no = models.CharField(max_length=10, null=False, blank=False , validators=[is_basic_valid_indian_number] )  # Field for phone number
    email = models.EmailField()
    amount = models.TextField(max_length=19,null=True,blank=True)  # Assuming this is a longer text field


def __str__(self):
        return self.name + " - " + self.email