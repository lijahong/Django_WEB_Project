from django import forms
from board.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','contents') #어떤 것을 입력받을지

