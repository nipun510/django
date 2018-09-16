from django import forms
TOPIC_CHOICES = (
     ('guest', 'guest'),
    ('admin', 'admin'),
    ('registered', 'registered'),
)
class ContactForm(forms.Form):
    topic = forms.ChoiceField(label='User Category', choices=TOPIC_CHOICES)
    name = forms.CharField(label='Your name', max_length=100)
    sender = forms.EmailField(label='Email ID', required=False)
    message = forms.CharField(widget=forms.Textarea())
    
class UserCreationForm(forms.Form):
    username = forms.CharField(label='Username', required=True)
    password = forms.CharField(label='Password', required= True)
    email    = forms.EmailField(label = 'Email', required = True)