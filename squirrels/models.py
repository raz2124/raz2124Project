from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    
    #at 3:30 in 8.9 he said id should auto generate - Django should do that

    name = models.CharField(
           max_length=100,
           help_text=_('Name of pet)',
    )
    
    date = models.DateField( 
         help_text=_('Day the Squirrel was Sighted'),
    )   

    date = models.DateField(
         help_text=_('Day the Squirrel was Sighted'),
    )
