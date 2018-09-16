from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


# Create your views here.
from django.core.mail import send_mail
from .forms import ContactForm
from .forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from django.conf.urls import url, include
from rest_framework import serializers, viewsets, routers

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')


# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer




def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            #new_user = form.save()
            user = User.objects.create_user(form.cleaned_data['username'],  form.cleaned_data['email'], form.cleaned_data['password'])
            return HttpResponseRedirect('/')
    else:
        form = UserCreationForm()
    return render(request, "users/register.html", {
        'form': form,
    })

def user_login(request):
    context = RequestContext(request)
    if request.method == 'POST':
          username = request.POST['username']
          password = request.POST['password']
          user = authenticate(username=username, password=password)
          if user is not None:
              if user.is_active:
                  login(request, user)
                  # Redirect to index page.
                  return HttpResponseRedirect("/")
              else:
                  # Return a 'disabled account' error message
                  return HttpResponse("You're account is disabled.")
          else:
              # Return an 'invalid login' error message.
              print("invalid login details " + username + " " + password)
              return render_to_response('users/login.html', {}, context)
    else:
        # the login is a  GET request, so just show the user the login form.
        return render(request, 'users/login.html', {}, context)


def user_logout(request):
    context = RequestContext(request)
    logout(request)
    # Redirect back to index page.
    return HttpResponseRedirect('/')


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            group = form.cleaned_data['category']
            name =  group = form.cleaned_data['name']
            message = form.cleaned_data['message']
            sender = form.cleaned_data.get(sender, 'nipunkumar66@gmail.com')
            send_mail('Feedback from your site, topic : {0}'.format(topic),message, sender, ['nipunkumar510@gmail.com'])
            return render_to_response('users/contact_response.html')
    else:
        form = ContactForm()
    return render(request, 'users/contact.html', {'form':form})