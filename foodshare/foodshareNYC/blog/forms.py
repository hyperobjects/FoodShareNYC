
from django import forms
from .models import Measurement, Post 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        'title', 'content', 'image']

class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('destination',)