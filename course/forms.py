from django import forms
from .models import *


class CommentForm(forms.ModelForm):
    class Meta:
        model = CourseComment
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'message-text'})
        }


class CommentTaskForm(forms.ModelForm):
    class Meta:
        model = TaskComment
        fields = ['text', ]
        widgets = {
            'text': forms.Textarea(attrs={'class': 'form-control', 'id': 'message-text'})
        }