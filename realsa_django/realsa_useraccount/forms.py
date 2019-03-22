from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class RealsaBlogRegisterUser(forms.Form):
    # In the blog only username, email and password are used. Username is derived
    # from email address. Log in function to enable comments and register to
    # mailing list are available. May have to add dummy values later.

    blog_username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Screen name'}), label='', max_length=240)
    blog_email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}), label='', max_length=240)
    blog_password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': ''}), label='Password:', max_length=120)
    is_mailinglist = forms.BooleanField(label='Mailinglist') #group
    is_comments = forms.BooleanField(label='Comments') #group

