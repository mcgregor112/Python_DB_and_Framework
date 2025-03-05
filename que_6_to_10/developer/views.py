from django.shortcuts import render
from developer.models import developers
from developer.forms import RegistrationForm

def developer_list_view(request):
    developer_list = developers.objects.all()
    return render(request,'dashboard/developer_list.html',{'developers' : developer_list})

def home_view(request):
    return render(request, 'dashboard/home.html')

def contact_view(request):
    return render(request, 'dashboard/contact.html')

def register_view(request):
    form = RegistrationForm()
    return render(request, 'dashboard/register.html', {'form': form})
