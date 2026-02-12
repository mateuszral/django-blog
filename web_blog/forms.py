from django import forms

from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ("title", "content")
        widgets = {
            "title": forms.TextInput(attrs={"id": "title", "placeholder": "Enter the title of your post"}),
            "content": forms.Textarea(attrs={"id": "content", "rows": 5, "placeholder": "Write your content here..."}),
        }