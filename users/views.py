from email import message
from click import password_option
from django.shortcuts import render, redirect
from torch import negative
from .forms import UserRegisterForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
#import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score


import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from keras.models import Sequential
from keras.layers import Dense
#from django.contrib.auth.models import authenticate , login 
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, 'users/home.html')

def admin(request):
    return render(request, 'admin')

def contact(request):
    #return HttpResponse('hi')
    return render (request, 'contact.html')

def about(request):
    #return HttpResponse('hi')
    return render (request, 'about.html')

def register(request):
    if request.method == "POST":
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Hi {username}, your account was created successfully')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})



@login_required()
def profile(request):
    return render(request, 'users/profile.html')

@login_required()
def result(request):
    dataset=pd.read_csv(r'C:\Users\sis14\OneDrive\Bureau\AI\django\doctor\templates\pima-indians-diabetes.csv',names=['Pregnancies','Glucose','BloodPressure','SkinThickness','Insulin','BMI','DiabetesPedigreeFunction','Age','Outcome'])
    dataset.head()

    dataset.isna().sum() 
    dataframeInNumpy = dataset.values #take the datarame to a numpy typed nd-array
    inputVariables = dataframeInNumpy[:,:8]
    outputVariables = dataframeInNumpy[:,8:]

    model = Sequential()
    model.add(Dense(15, input_dim=8, kernel_initializer='random_uniform', activation='relu'))
    model.add(Dense(7, input_dim=8, kernel_initializer='random_uniform', activation='relu'))
    model.add(Dense(1, input_dim=8, kernel_initializer='random_uniform', activation='sigmoid'))
    #model = Sequential()
    #model.add(Dense()) 
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    #model.fit(inputVariables,outputVariables)
    model.fit(inputVariables,outputVariables,epochs=770,batch_size=512)
    scores = model.evaluate(inputVariables,outputVariables)
    print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))

    
    val1 = float(request.POST.get('n1' , False)) 
    val2 = float(request.POST.get('n2' , False)) 
    val3 = float(request.POST.get('n3' , False)) 
    val4 = float(request.POST.get('n4' , False)) 
    val5 = float(request.POST.get('n5' , False)) 
    val6 = float(request.POST.get('n6' , False)) 
    val7 = float(request.POST.get('n7' , False)) 
    val8 = float(request.POST.get('n8' , False)) 

    pred = model.predict([[val1, val2, val3, val4, val5, val6, val7, val8]])
    print('accurency is ',pred)
    result1 = ""
    if pred>[0.5]:
        result1= "positif result please contact us"
    else:
        result1 = "felicitation negative result"
        
    if request.method == 'POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        result1=Result1(
            rzlt=result1,
            username=username,
            email=email
        ) 
        x=0
        x = Result1.objects.filter(username=username).count()
        #print(username , x) 
        result1.save()
       
    if pred>[0.5]:    
        data ={
        'result1': result1,
        'username':username,
        'email':email
        }
        
        message='''
        username: {}
        result: {}  
        email: {} 
        '''.format(data['username'],data['result1'],data['email'])
        send_mail(data['result1'],message,'',[email]) 
        result1.save()    
           
    return render(request, 'home.html',{"result2":result1})
#=========================ntestyy==============================#
from .models import Result1
#==========================================================#
from django.shortcuts import render, redirect
from .models import Contact
from django.core.mail import send_mail
def contact(request):
    if request.method == 'POST':
        name=request.POST.get('name')
        mobileC=request.POST.get('mobileC')
        email=request.POST.get('email')
        message=request.POST.get('message')
        
        contact=Contact(
            name=name,
            mobileC=mobileC,
            email=email,
            message=message,
            
            
        )
        data ={
            'name': name,
            'mobileC':mobileC,
            'message':message,
            'email':email
        }
        message='''
        name: {}
        mobile : {}
        from: {}
        new msg: {}    
        '''.format(data['name'],data['mobileC'],data['email'],data['message'])
        send_mail(data['message'],message,'',['predectydiabete@gmail.com'])

        contact.save()
        messages.success(request, f'Hi {name}, your message was delevired our team will check it within 2 works days')
        return redirect('home')
    return render(request,'users/contact.html')





from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
from .models import Result1
from django.core import serializers

'''def dashboard_with_pivot(request):
    return render(request, 'dashboard_with_pivot.html', {})'''


def test(request):
    dataset = Result1.objects.all()
    return render(request,'data.html',{'test': dataset})

def dashboard_with_pivot(request):
    n = Result1.objects.filter(rzlt='felicitation negative result').count()
    p = Result1.objects.filter(rzlt='positif result please contact us').count()
    context = {
        'n':n,
        'p':p
    }   
    return render(request,'dashboard_with_pivot.html',context)


'''def test(request):
    dataset = Result1.objects.all()
    x = Result1.objects.filter(username='achraf').count()
    x=x
    print(x)
    username=Result1.objects.filter(username='achraf')
    nbtest=nbtest(
        
        username=username,
        nb=x
    ) 
    x=0
    x = Result1.objects.filter(username=username).count()
        #print(username , x) 
    print(x)
    nbtest.save()
    return render(request,'data.html',{'test': dataset})'''

'''
from django.shortcuts import render
from .utils import*
from django.contrib.auth.models import User
from .models import *
import uuid
from .utils import *
def register(request):
    if request.method =='POST':
        email=request.POST.get('email')
        password=request.POST.get('password')
        user_obj = User (username = email)
        user_obj.set_password(password)
        user_obj.save()
        #User.save()
        #User= User.save()
        p_obj=Profile.objects.create(
            user=user_obj,
            email_token = str(uuid.uuid4())
        )
        send_email_token(email,p_obj.email_token)
    return render(request,'users/register.html')

def verify(request ,token):
    try:
        obj = Profile.objects.get(email_token = token)
        obj.is_verified = True
        obj.save()
        return HttpResponse('verified')

    except Exception as e:
        return HttpResponse('non verified')
'''
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserRegisterForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def home(request):
    return render(request, 'home.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            message = render_to_string('acc_active_email.html', {
                'user':user, 'domain':current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': account_activation_token.make_token(user),
            })
            # Sending activation link in terminal
            # user.email_user(subject, message)
            mail_subject = 'Activate your Predecty account.'
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            #return HttpResponse('Please confirm your email address to complete the registration.')
            messages.success(request, f'Hi {user}, Please confirm your email address to complete the registration.')
            return redirect('home')
            # return render(request, 'acc_active_sent.html')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        messages.success(request, f'Hi {user}, your account activated')
        return redirect('home')
    else:
        messages.success(request, f'Hi {user}, your account not activate re-signup or contact us')
        return redirect('home')


from django.urls import reverse
from .forms import EditProfileForm
def edit_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)

        if form.is_valid():
            form.save()
            return redirect(reverse('profile'))
    else:
        form = EditProfileForm(instance=request.user)
        args = {'form': form}
        return render(request, 'edit_profile.html', args)
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)

        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect(reverse('profile'))
        else:
            return redirect(reverse('change_password'))
    else:
        form = PasswordChangeForm(user=request.user)

        args = {'form': form}
        return render(request, 'change_password.html', args)