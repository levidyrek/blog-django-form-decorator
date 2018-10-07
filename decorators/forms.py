from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import gettext as _


class PersonForm(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    age = forms.IntegerField()

    def clean_first_name(self):
        first_name = self.cleaned_data['first_name']
        return self._clean_name(first_name)

    def clean_last_name(self):
        last_name = self.cleaned_data['last_name']
        return self._clean_name(last_name)

    def _clean_name(self, name):
        if len(name) < 2:
            raise ValidationError(
                _('Must be at least two characters.')
            )
        return name

    def clean_age(self):
        age = self.cleaned_data['age']
        if age < 0:
            raise ValidationError(_('Must not be negative.'))
        return age
