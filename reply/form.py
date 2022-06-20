from django import forms
from reply.models import Reply

class Replyform(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('contents',)
        exclude = ('writer',)
