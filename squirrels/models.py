from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    #at 3:30 in 8.9 he said id should auto generate - Django should do that
    name = models.CharField(
           max_length=100,
           help_text=_('Name of pet'),
    )
   
    latitude = models.DecimalField(
            max_digits=5,
            decimal_places=2,
            null=True,
    )

    longitude = models.DecimalField(
            max_digits=5,
            decimal_places=2,
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
            help_text=('Time of Day'),
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
            help_text=('How old was this squirrel'),
            choices=AGE_CHOICES,
            default=AM,
    )

    date = models.DateTimeField( 
        help_text=_('Day the Squirrel was Sighted'),
        auto_now_add=True,
    )
    
    def  __str__(self):
        return self.name


#class Sighting(models.Model):
#    squirrel = models.ForeignKey(
#            'sighting.Squirrel',
#            on_delete=models.CASCADE,
#            )
#
#    def __str__(self):
#        return f'{self.sighter] at {self.create_ts}'
