from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):

    unique_id = models.CharField(
           max_length=20,
           null=True
    )
   
    latitude = models.DecimalField(
            max_digits=17,
            decimal_places=15,
            null=True,
    )

    longitude = models.DecimalField(
            max_digits=17,
            decimal_places=15,
            null=True,
    ) 

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM, _('PM')),

    ]

    shift = models.CharField(
            max_length=20,
            choices=SHIFT_CHOICES,
            default=AM,
    )
    
    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    QUESTION = '?'

    AGE_CHOICES = [
            (ADULT, _('Adult')),
            (JUVENILE, _('Juvenile')),
            (QUESTION, _('?')),
    ]

    age = models.CharField(
            max_length=20,
            choices=AGE_CHOICES,
            default=ADULT,
    )

    date = models.DateField( 
        null=True,
    )
    
    def  __str__(self):
        return self.unique_id

