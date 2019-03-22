from django.shortcuts import render, redirect
#from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib import messages

from .forms import RealsaBlogRegisterUser

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RealsaBlogRegisterUser(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            #form.save

            # form variable extraction
            username = form.cleaned_data.get('blog_username')
            email = form.cleaned_data.get('blog_email')
            password = form.cleaned_data.get('blog_password')
            is_mailinglist = form.cleaned_data.get('is_mailinglist')
            is_comments = form.cleaned_data.get('is_comments')

            # make a new user
            user = User.objects.create_user(username, email, password)
            #user.save

            # add user to groups
            

            messages.success(request, f'Account created for {username}')


            # redirect to a new URL:
            return redirect('blog')
            #return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = RealsaBlogRegisterUser()

    return render(request, 'realsa_useraccount/name.html', {'form': form})




#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save
#            username = form.cleaned_data.get('username')
#            messages.success(request, f'Account created for {username}')
#            return redirect('blog')
#    else:
#        form = UserCreationForm()
#    return render(request, 'realsa_useraccount/register.html', {'form': form})

#def register(request):
#    if request.method == 'POST':
#        form = UserCreationForm(request.POST)
#        if form.is_valid():
#            form.save
#            username = form.cleaned_data.get('username')
#            messages.success(request, f'Account created for {username}')
#            return redirect('blog')
#    else:
#        form = UserCreationForm()
#    return render(request, 'realsa_useraccount/register.html', {'form': form})