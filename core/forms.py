from django import forms
from .models import SemesterResult, Subject
from django.forms import inlineformset_factory

class SemesterForm(forms.ModelForm):
    class Meta:
        model = SemesterResult
        fields = ['semester_name']

class SubjectForm(forms.ModelForm):
    class Meta:
        model = Subject
        fields = ['name', 'mark', 'credit']

SubjectFormSet = inlineformset_factory(
    SemesterResult,
    Subject,
    form=SubjectForm,
    extra=6,
    can_delete=False
)
