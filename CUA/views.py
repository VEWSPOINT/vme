from django.shortcuts import render, redirect
from CUA.forms import customerForm, customerAddForm, developerForm, developerAddForm
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from CUA.models import Customer, Developer
from django.contrib.auth.models import User


# Create your views here.

def index_views(request):
    return render(request, 'Home/home.html')


@login_required
def userLogout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index_view'))


def register(request):
    return render(request, 'CUA/register.html')


def registerCustomer(request):
    registered = False
    if request.method == 'POST':
        var_customerForm = customerForm(request.POST)
        var_customerAddForm = customerAddForm(request.POST)
        if var_customerForm.is_valid() and var_customerAddForm.is_valid():
            customerprimary = var_customerForm.save()
            customerprimary.set_password(customerprimary.password)
            customerprimary.save()
            customerAdd = var_customerAddForm.save(commit=False)
            customerAdd.customer = customerprimary
            customerAdd.save()
            registered = True
    else:
        var_customerForm = customerForm()
        var_customerAddForm = customerAddForm()
    return render(request, 'CUA/registerCustomer.html',
                  {'var_customerForm': var_customerForm, 'var_customerAddForm': var_customerAddForm,
                   'registered': registered})


def registerDeveloper(request):
    registered = False
    if request.method == 'POST':
        var_developerForm = developerForm(request.POST)
        var_developerAddForm = developerAddForm(request.POST)
        if var_developerForm.is_valid() and var_developerAddForm.is_valid():
            developerprimary = var_developerForm.save()
            developerprimary.set_password(developerprimary.password)
            developerprimary.save()
            developerAdd = var_developerAddForm.save(commit=False)
            developerAdd.developer = developerprimary
            developerAdd.save()
            registered = True
    else:
        var_developerForm = developerForm()
        var_developerAddForm = developerAddForm()
    return render(request, 'CUA/registerDeveloper.html',
                  {'var_developerForm': var_developerForm, 'var_developerAddForm': var_developerAddForm,
                   'registered': registered})


def userLogin(request):
    invalidlogin = False
    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('dashboard'))
            else:
                return HttpResponse('Account not active')
        else:
            invalidlogin = True
            return redirect('/CUA/login/')

    else:

        return render(request, 'CUA/login.html', {'invalidlogin': invalidlogin})


@login_required
def dashboard(request):
    try:
        current = Customer.objects.get(customer=request.user)
    except Customer.DoesNotExist:
        current = Developer.objects.get(developer=request.user)
    if current.is_customer:
        return redirect('/customerDash/')
    else:
        return redirect('/developerDash/')
    return render(request, 'CUA/dashboard.html')


def customerDash(request):
    return render(request, 'CUA/customerDash.html')


def developerDash(request):
    return render(request, 'CUA/developerDash.html')
