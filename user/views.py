from django.shortcuts import render,redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login as auth_login , logout 
from django.contrib.auth.models import User
from . forms import UpdateUser
from django.views.decorators.cache import cache_control
from .forms import*#.............
from django.contrib.auth.decorators import login_required#...............

# Create your views here.


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signup(request):
    if request.method == 'POST':
        input_username = request.POST['username']
        input_password = request.POST['password']
        if not input_username or not input_password:
            messages.error(request,'Enter username and password')
            return render (request,'signup.html')
       
        objUser = User.objects.create_user(username=input_username,password=input_password)
        objUser.save()
        return redirect('login_page')
    return render(request,'signup.html')
  

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def login(request):
    if request.user.is_authenticated:
        return redirect("home_page")
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            messages.error(request,'Enter username and password')
            return render(request, 'login.html')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            request.session['user_id']=user.id
            auth_login(request, user)
            return redirect('home_page')
        else:
            messages.error(request, 'Invalid username or password')
    return render(request, 'login.html',)


# @login_required(login_url='login_page')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def home(request):
    if not request.user.is_authenticated:
        return redirect("login_page")
    user_id =     request.session['user_id']
    user = User.objects.get(id=user_id)
    username = user.username
    return render (request,'home.html',{'username':username})


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminlogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        if not username or not password:
            messages.error(request,'Enter username and password')
            return render(request,'adminlogin.html')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['user_id']=user.id
            auth_login(request, user)
            return redirect('adminDashboard')
        else:
            messages.error(request, 'Invalid Admin ID or password')
    return render (request,'adminlogin.html')
@login_required(login_url='admin')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminDashboard(request):
    user_set = User.objects.filter(is_superuser=False)
    admin_id = request.session['user_id']
    admin= User.objects.get(id=admin_id)
    admin_name = admin.username
    return render(request,'adminDashboard.html',{'userlist':user_set, 'admin_name':admin_name} )

def edit(request,pk):
    user_to_be_editted = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateUser(request.POST, instance=user_to_be_editted)
        if form.is_valid():
            form.save()
            return redirect('adminDashboard')
    else:
        form = UpdateUser(instance=user_to_be_editted)
    return render(request,'edit.html', {'form':form, 'user': user_to_be_editted} )

def delete(request,pk):
    instance= User.objects.get(pk=pk)
    instance.delete()
    user_set = User.objects.filter(is_superuser=False)
    return render(request,'adminDashboard.html',{'userlist':user_set} )


@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def signout(request):
    logout(request)
    return redirect('login_page')
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def adminsignout(request):
    logout(request)
    return redirect('admin')

def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET.get('keyword')
        user_set = User.objects.filter(username__icontains=keyword)
       
        
    context={
        'userlist': user_set,
    }
    return render(request, 'adminDashboard.html', context)