from django.forms import ModelForm, CharField, IntegerField, TimeField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit, Field

from .models import Pres


class PresForm(ModelForm):
    name = CharField(label="Name")
    max_members = IntegerField(min_value=0, label="Anzahl Teilnehmer")
    room = IntegerField(min_value=0, label="Raum")
    start_time = TimeField(label="Startzeit")
    end_time = TimeField(label="Endzeit")

    class Meta:
        model = Pres
        fields = ['max_members', 'room', 'start_time', 'end_time']

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Fieldset(
                'Neues Formular',
                'name',
                'max_members',
                'room',
                Field(
                    'start_time',
                    css_class="datepicker",
                    autocomplete="off",
                ),
                Field(
                    'end_time',
                    css_class="datepicker",
                    autocomplete="off",
                ),
            ),
            ButtonHolder(
                Submit('submit', 'Submit', css_class='button green pull-right'),
                )
        )
        super(PresForm, self).__init__(*args, **kwargs)
