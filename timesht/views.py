from django.shortcuts import render
from timesht.models import EName
from django.http import HttpResponseRedirect

from .forms import NameForm

def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        print("You've clicked the button so this is a post request")
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required

            name = request.POST.get('your_name')
            #formObj = EName.objects.create(Name=name)
            form_object = EName.objects.get(Name=name)
            print(dir(form_object))
            # redirect to a new URL:
            #Adding a comment to test git
            return HttpResponseRedirect('thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        print("This is the first time hence I'm doing nothing just returning the form")
        form = NameForm()

    return render(request, 'name.html', {"form":form, "test_var":"Testing variable"})

def thank_you(request):
    return render(request, 'thank_you.html', {})

def login(request):
    return render(request, 'login.html', {})