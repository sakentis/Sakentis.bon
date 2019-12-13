from django.shortcuts import render
from django.contrib import auth
from django.views import generic
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy

class Register(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register/signup.html'

# def signup(request):
    # if request.method == 'POST':
    #     # user has info and wants to account now
    #     if request.POST['password1'] == request.POST['password2']:
    #         try:
    #             user = User.objects.get(username=request.POST['username'])
    #             return render(request, 'accounts/signup.html',{'error':'Username has been used already'})
    #         except User.DoesNotExist:
    #             user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
    #             auth.login(request, user)
    #             return redirect('home')
    # else:
    #     # user wants to enter info
    #     return render(request, 'accounts/signup.html')

# def login(request):
#     return render(request, 'accounts/login.html')
#
# def logout(request):
#     # TODO need to route to home page
#     # and don't forget to log out
#     return render(request, 'accounts/signup.html')