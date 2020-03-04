from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    title = forms.CharField(label='', required=False, widget=forms.TextInput(
        attrs={'class': 'form-control-sm', 'Placeholder': 'Title' }))
    content = forms.CharField(label='', required=True, widget=forms.Textarea(
        attrs={'rows': 2, 'class': 'form-control-sm', 'Placeholder': 'Message'}))
    image = forms.FileField(label='Image')

    class Meta:
        model = Post
        fields = [
                  'title',
                  'content',
                  'image'
                  ]
