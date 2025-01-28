from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['author', 'content']
        labels = {
            'author': '',
            'content': ''
        }

        widgets = {
            'author': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نام'
                }
            ),
            'content': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'نظر شما',
                    'id': 'message',
                    'rows': 10,
                    'cols': 40
                }
            ),
        }

        error_messages = {
            'author': {
                'required': 'پر کردن این فیلد الزامی است'
            },
            'content': {
                'required': 'پر کردن این فیلد الزامی است'
            }
        }
