from django.forms.models import ModelForm
from letters.models import Letter


class LetterForm(ModelForm):

    class Meta:
        model = Letter