from django import forms
from recip.models import Comments, Recip


class CommentsForms(forms.ModelForm):
    class Meta:
        model = Comments
        fields = (
            'text'
        )


class RecipForms(forms.ModelForm):
    class Meta:
        model = Recip
        fields = (
            'text',
            'title'
        )