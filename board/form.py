from django import forms
from board.models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title','contents') #어떤 것을 입력받을지
        exclude = ('writer',) #form에서 writer를 제외시킨다. 즉, 입력받지 않는다


