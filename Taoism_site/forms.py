# forms.py
from django import forms
from .models import Post, Blog_Category

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'excerpt', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': '文章标题'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '文章内容', 'rows': 10}),
            'excerpt': forms.Textarea(attrs={'class': 'form-control', 'placeholder': '文章摘要（可选）', 'rows': 3}),
            'category': forms.Select(attrs={'class': 'form-control'})
        }