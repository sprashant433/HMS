from django.shortcuts import render
from .models import Userinfo
from .Reg_form import RegForm
from faker import Faker

from . import Check_Form


# Create your views here.


def index(request, temp_flag=0):
    return render(request, 'Hospital_app/index.html', {'flag': temp_flag})


def commoninfo(request):
    return render(request, 'Hospital_app/commoninfo.html')


def adduserinfo(request):
    form = RegForm()
    fakegen = Faker()
    user_list = Userinfo.objects.order_by('First_Name')
    fake_id = fakegen.bothify(text='????-########')
    for item in user_list:
        if item.uniqueID == fake_id:
            fake_id = fakegen.bothify(text='????-########')
        else:
            break

    temp_flag = 0
    if request.method == "POST":
        form = RegForm(request.POST)
        if form.is_valid() and form.cleaned_data['Password'] == form.cleaned_data['Confirm_Password']:
            form.save(commit=True)
            temp_flag = 1
            return index(request, temp_flag)
        elif form.cleaned_data['Password'] != form.cleaned_data['Confirm_Password']:
            form.add_error('Confirm_Password', 'The Passwords do not match')
        else:
            print('Something Input Goes Wrong!')
    return render(request, 'Hospital_app/regis.html', {'form': form, 'fakeid': fake_id})


def fetchuserinfo(request):
    check_form = Check_Form.CheckForm()
    temp_list = []
    user_list = Userinfo.objects.order_by('First_Name')
    flag = 0
    if request.method == 'POST':
        check_form = Check_Form.CheckForm(request.POST)

        if check_form.is_valid():
            for item in user_list:
                if item.uniqueID == check_form.cleaned_data['unique_id']:
                    flag = 1
                    temp_name = item.First_Name + " " + item.Last_Name
                    temp_id = str(item.uniqueID)
                    temp_dob = str(item.DOB)
                    temp_list.append(temp_name)
                    temp_list.append(temp_id)
                    temp_list.append(temp_dob)
                    break
                else:
                    flag = 22

    return render(request, 'Hospital_app/users.html', {'check_form': check_form, 'data': list(temp_list), 'flag': flag})
