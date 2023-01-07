<<<<<<< HEAD
from django import forms
from .models import ReviewRating

class ReviewForm(forms.ModelForm):
    class Meta:
        model = ReviewRating
        fields = ['subject', 'review', 'rating']



class bkashpayment(forms.ModelForm):
    class Meta:
        # model =payment
        filds = ['dept', 'doc', 'name','mail', 'date', 'transiction']
=======


from django import forms
class FAQForm(forms.Form):
    question = forms.CharField(label='Question', max_length=255)
    


class AnswerForm(forms.Form):
    answer = forms.CharField(label='Answer', widget=forms.Textarea)

>>>>>>> ec0decf4c99b40666db5361d45c290f3e7d31acc
