from django.forms import ModelForm

from .models import Squirrel

class AddSightingsForm(ModelForm):
    class Meta:
        model  = Squirrel
        fields  = [
            'latitude',
            'longitude',
            'unique_id',
            'shift',
            'age',
            'date',
        ]
