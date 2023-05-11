from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth  import authenticate,  login, logout
from django.contrib.auth.decorators import login_required
from .forms import ApplicationForm
from .models import Application, Notice, Detail
from django.views.generic import UpdateView
from .forms import CreateUserForm

def online_admission(request):
    return render(request, "online_admission.html")

def index(request):
    data = {
        'title': 'Home Page'
    }
    return render(request, "index.html", data)

def home(request):
     return render(request, "online_admission.html")

@login_required(login_url='login')
def products(request):
	products = Product.objects.all()

	return render(request, 'products.html', {'products':products})

# def admission_form(request):
#     return render(request, "admission_form.html")
def merit_list(request):
    return render(request, "merit_list.html")
def hostel(request):
    return render(request, "hostel.html")
def help_support(request):
    return render(request, "help_support.html")    

def college(request):
    notice = Notice.objects.all()
    return render(request, "college.html", {'notice':notice})

def notice(request, myid):
    notices = Notice.objects.filter(id=myid).first()
    details = Detail.objects.filter(title=notices)
    return render(request, "notice.html", {'details':details})

def application_form(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    hide = Application.objects.filter(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            application = form.save()
            application.user = request.user
            application.save()
            return render(request, "application_form.html")
    else:
        form=ApplicationForm()
    return render(request, "application_form.html", { 'form':form,'hide':hide})

def edit_application(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    try:
        application = request.user.application
    except Application.DoesNotExist:
        application = Application(user=request.user)
    if request.method=="POST":
        form = ApplicationForm(data=request.POST, files=request.FILES, instance=application)
        if form.is_valid():
            form.save()
            alert = True
            return render(request, "edit_application.html", {'alert':alert})
    else:
        form=ApplicationForm(instance=application)
    return render(request, "edit_application.html", {'form':form})

def status(request):
    if not request.user.is_authenticated:
        return redirect("/login")
    application = Application.objects.get(user=request.user) 
    return render(request, "status.html", {'application':application})

def registerPage(request):
    if request.user.is_authenticated:
        return redirect('online_admission')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'register.html', context)


def loginPage(request):
    if request.user.is_authenticated:
        return redirect('online_admission')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('online_admission')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)

def loggedout(request):
    logout(request)
    messages.success(request, "Successfully logged out")
    return redirect('/login')


def handle_admin(request):
    if not request.user.is_superuser:
        return redirect("/login")
    users = User.objects.all().count
    approve = Application.objects.filter(Application_Status='Approved').count
    reject = Application.objects.filter(Application_Status='Rejected').count
    pending = Application.objects.filter(Application_Status='Pending').count
    return render(request, "handle_admin.html", {'approve':approve, 'reject':reject, 'pending':pending, 'users':users})

def users(request):
    if not request.user.is_superuser:
        return redirect("/login")
    allUsers = Application.objects.all()
    return render(request, "users.html", {'allUsers':allUsers})

def student_application(request, myid):
    if not request.user.is_superuser:
        return redirect("/login")
    application = Application.objects.filter(id=myid)
    return render(request, "student_application.html", {'application':application[0]})

class UpdatePostView(UpdateView):
    model = Application
    template_name = 'application_status.html'
    fields = ('Application_Status', 'message',)

def approved_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    approved = Application.objects.filter(Application_Status="Approved")
    return render(request, "approved_applications.html", {'approved':approved})

def pending_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    pending = Application.objects.filter(Application_Status="Pending")
    return render(request, "pending_applications.html", {'pending':pending})

def rejected_applications(request):
    if not request.user.is_superuser:
        return redirect("/login")
    rejected = Application.objects.filter(Application_Status="Rejected")
    return render(request, "rejected_applications.html", {'rejected':rejected})