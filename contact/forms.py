from django import forms

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField( label='Your e-mail address')
    message = forms.CharField(widget=forms.Textarea)
     
   
