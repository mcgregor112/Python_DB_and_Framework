from django.shortcuts import render ,redirect
from django.contrib import messages
from login.models import crud


def login_view(request):
    if request.method == 'POST':
        email_ = request.POST.get('email')
        password_ = request.POST.get('password')

        try:
            user = crud.objects.get(email=email_, password=password_)
            request.session['user_id'] = user.id  # Ensure user_id is set
            messages.success(request, "Successfully logged in!")
            return redirect('home_view')
        except crud.DoesNotExist:
            messages.error(request, "Invalid email or password.")

    return render(request, 'login/login.html')



def register_view(request):
    if request.method == 'POST':
        name_ = request.POST.get('name')
        email_ = request.POST.get('email')
        password_ = request.POST.get('password')

        if name_ and email_ and password_:
            if not crud.objects.filter(email=email_).exists():
                crud.objects.create(
                    name = name_,
                    email = email_,
                    password = password_
                )
                messages.success(request , "register successfull !")
                return redirect('login_view')
            else :
                messages.error(request, "email is alredy exist !")
        else:
            messages.error(request,"reqired all fildes ")            

    return render(request, 'login/register.html')

def home_view(request):
    user_id = request.session.get('user_id')  

    if not user_id:  
        messages.error(request, "You must be logged in.")
        return redirect('login_view')  
    try:
        user = crud.objects.get(id=user_id)
    except crud.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login_view')

    return render(request, 'login/home.html', {'user': user})



def profile_view(request):
    user_id = request.session.get('user_id')  

    if not user_id:  
        messages.error(request, "You must be logged in.")
        return redirect('login_view')
    try:
        user = crud.objects.get(id=user_id)
    except crud.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('login_view')

    return render(request, 'login/profile.html', {'user': user})



def update_view(request ,id):
    user_id = request.session.get('user_id')
    user = crud.objects.get(id=user_id)

    if request.method == 'POST':
        new_name = request.POST.get('name')

        if new_name:
            user.name = new_name
            user.save()
            messages.success(request , "update success")
            return redirect('profile_view')
        else:
            messages.error(request, "name not empty")    

    return render(request,'login/update.html',{'user' :user})

def delete_account(request, id):
    try:
        user = crud.objects.get(id=id)
    except crud.DoesNotExist:
        messages.error(request, "User not found.")
        return redirect('profile_view') 
    if request.method == 'POST':
        user.delete()
        messages.success(request, "Deleted successfully!")
        return redirect('register_view')

    return render(request, 'login/delete.html', {'user': user})





