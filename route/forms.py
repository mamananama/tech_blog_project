from django import forms
from .models import Route, Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'file', 'image')


class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('name', 'status')
        widgets = {
            'status': forms.RadioSelect(),
        }


class RouteEditForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ('status',)
        widgets = {
            'status': forms.RadioSelect(),
        }
