from django import forms
from Game_Distribution.models import UserModel

class Userforms(forms.ModelForm):
    class Meta:
        model=UserModel
        fields="__all__"