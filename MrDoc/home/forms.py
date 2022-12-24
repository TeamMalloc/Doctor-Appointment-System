

from django import forms
class FAQForm(forms.Form):
    question = forms.CharField(label='Question', max_length=255)
    


class AnswerForm(forms.Form):
    answer = forms.CharField(label='Answer', widget=forms.Textarea)

