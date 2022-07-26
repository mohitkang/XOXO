from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.views.generic import TemplateView
# Create your views here.
def home(request):
  return render(request,"authentication/index.html")


def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']
        myuser = User.objects.create_user(username, email, pass1)
        
        myuser.save()
        messages.success(request, "Your Account has been created succesfully!!")
        return redirect('signin')
         

    return render(request,"authentication/signup.html")

def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['pass1']
        
        user = authenticate(username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            # fname = user.first_name
            # messages.success(request, "Logged In Sucessfully!!")
            if username == 'admin':
                if pass1 == '123':
                  return render(request, "authentication/upload.html")
            else:    
             return render(request, "authentication/index.html")
        else:
            messages.error(request, "Bad Credentials!!")
            return redirect('home')
    

    return render(request,"authentication/signin.html")

def signout(request):
    logout(request)
    messages.success(request, "Logged Out Successfully!!")
    return redirect('home')

#from here changes are done(not competed)
#def upload(request):
    #context = {}
 #   if request.method == 'POST':
  #      uploaded_file = request.FILES['document']
   #     print(uploaded_file.name)
    #    print(uploaded_file.size)
       # fs = FileSystemStorage()
       # name = fs.save(uploaded_file.name, uploaded_file)
       # context['url'] = fs.url(name)
   # return render(request, 'upload.html')
