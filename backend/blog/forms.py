from attr import fields
from django.forms import ModelForm

from .models import *


class postForm(ModelForm):

    class Meta:
        model = post
        fields = '__all__'