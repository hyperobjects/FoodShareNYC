
from django import forms
from .models import Measurement, Post 


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        'title', 'image', 'content',  'location']

class MeasurementModelForm(forms.ModelForm):
    class Meta:
        model = Measurement
        fields = ('destination',)