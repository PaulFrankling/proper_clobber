""" Blog forms.py """
from django import forms
from .widgets import CustomClearableFileInput
from .models import BlogPost


class BlogForm(forms.ModelForm):
    """ Form to create blog post """
    class Meta:
        model = BlogPost
        fields = '__all__'

    image = forms.ImageField(
        label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'rounded-0'
