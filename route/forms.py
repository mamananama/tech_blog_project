from pyexpat import model
from froala_editor.widgets import FroalaEditor
from django import forms
from .models import Route, Post, Comment, Page


class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['title'].widget.attrs = {
            'class': 'post-form-title  shadow-bottom-inset'
        }
        self.fields['title'].label = '제목'
        self.fields['content'].widget.attrs = {
            'class': 'post-form-content shadow-bottom-inset'
        }
        self.fields['content'].label = '내용'
        self.fields['file'].widget.attrs = {
            'class': 'post-form-file'
        }
        self.fields['file'].label = '첨부파일'
        self.fields['image'].widget.attrs = {
            'class': 'post-form-image'
        }
        self.fields['image'].label = '이미지'

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


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ("message",)

        widgets = {
            'message': forms.TextInput(),
        }
        labels = {
            'message': '',
        }


class PageForm(forms.ModelForm):
    class Meta:
        model = Page
        content = forms.CharField(widget=FroalaEditor)
