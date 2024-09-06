from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from App.models import *
from MyTemplatesApp.forms import *
from django.http import HttpResponse,HttpResponseRedirect
from datetime import datetime, timedelta
#import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator


from django.contrib import messages
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, DetailView, DeleteView, UpdateView, ListView

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
#C:\Users\DIMOSO JR\Desktop\ProjectWork\SmartInvigilation\SmartInvigilationProject\SmartInvigilationApp
print(BASE_DIR)
from django.core.files.base import ContentFile

from django.template.loader import get_template
from xhtml2pdf import pisa
from django.contrib.staticfiles import finders

#from .resources import *
from tablib import Dataset

import datetime

import csv
from datetime import datetime, timedelta
from django.utils.timezone import now
import time as tm
from django.conf import settings
from django.core.mail import send_mail

def Mylogin_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        
        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            

            redirect_url = request.GET.get('next', 'Mylogin_user')
            return redirect(redirect_url)
        else:
            messages.error(request, "Username Or Password is incorrect!!",
                           extra_tags='alert alert-warning alert-dismissible fade show')

    return render(request, 'MyTemplatesApp/login.html')


def Mylogout_user(request):
    logout(request)
    return redirect('Mylogin_user')

# def create_user(request):

#     if request.method == 'POST':
#         username = request.POST.get('username')
#         email = request.POST.get('email')
#         password = request.POST.get('password')
#         password2 = request.POST.get('password2')
#         Course = request.POST.get('Course')
#         Year = request.POST.get('Year')
#         #role = request.POST['role']

#         if password == password2:
#             if MyUser.objects.filter(email=email).exists():
#                 messages.info(request, f"Email {email} Already Taken")
#                 return redirect('register')
#             elif MyUser.objects.filter(username=username).exists():
#                 messages.info(request, f"Username {username} Already Taken")
#                 return redirect('register')
#             else:
#                 user = MyUser.objects.create_user(
#                     username=username, 
#                     email=email, 
#                     password=password, 
#                     Course=Course, 
#                     Year=Year
#                     )
#                 user.save()


#                 #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
#                 username = request.POST.get('email')
#                 #last_name = request.POST['last_name']
#                 email = request.POST.get('email')
#                 subject = "Welcome To Students Polling System"
#                 message = f"Ahsante  {username} kwa kujisajili kwenye mfumo wetu kama {username} email yako {email} "
#                 from_email = settings.EMAIL_HOST_USER
#                 recipient_list = [email]
#                 send_mail(subject, message, from_email, recipient_list, fail_silently=True)



                

                
#                 return redirect('login')
#         else:
#             messages.info(request, 'The Two Passwords Not Matching')
#             return redirect('register')

#     else:
#         return render(request, 'accounts/register.html')



def MyUserRegistrationView(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            
            email = request.POST.get('email')
            username = request.POST.get('username')

            
            #HIZI NI KWA AJILI KUTUMA EMAIL ENDAPO MTU AKIJISAJILI
            
            subject = "Karibu Mfugaji Smart"
            message = f"Ahsante  {username} kwa kujisajili kwenye mfumo wetu kama {username} email yako {email} "
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)


            messages.success(request, f'{username} is registered successfully')
            return redirect('Mylogin_user')
    else:
        form = UserRegistrationForm()

    context = {
        "form": form
    }
    return render(request, 'MyTemplatesApp/register.html', context)

# def create_user(request):
#     if request.method == 'POST':
#         check1 = False
#         check2 = False
#         check3 = False
#         form = UserRegistrationForm(request.POST)
#         if form.is_valid():
#             username = form.cleaned_data['username']
#             password1 = form.cleaned_data['password1']
#             password2 = form.cleaned_data['password2']
#             email = form.cleaned_data['email']

#             if password1 != password2:
#                 check1 = True
#                 messages.error(request, 'Password doesn\'t matched')
#             if User.objects.filter(username=username).exists():
#                 check2 = True
#                 messages.error(request, 'Username already exists')
#             if User.objects.filter(email=email).exists():
#                 check3 = True
#                 messages.error(request, 'Email already registered')

#             if check1 or check2 or check3:
#                 messages.error(
#                     request, "Registration Failed")
#                 return redirect('register')
#             else:
#                 user = User.objects.create_user(
#                     username=username, password=password1, email=email)
#                 messages.success(
#                     request, f'Thanks for registering {user.username}!')
#                 return redirect('login')
#     else:
#         messages.info(
#                     request, f'Registration failed!')
#         form = UserRegistrationForm()
#     return render(request, 'accounts/register.html', {'form': form})






@login_required(login_url='Mylogin_user')
def AllKumbushoLaChanjo(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoLaChanjoSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoLaChanjo.objects.all(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).order_by('-id')




    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = KumbushoLaChanjoSearchForm(request.POST or None)




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        #category__icontains=form['category'].value(),
        AinaYaKuku = form['AinaYaKuku'].value()

        

                                        
        queryset = KumbushoLaChanjo.objects.filter(
                                        username__icontains=form['username'].value(),
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            )
        if (AinaYaKuku != ''):
            queryset = KumbushoLaChanjo.objects.all(
                   #Year__id__icontains = yearId.id,
                )
            queryset = queryset.filter(AinaYaKuku_id=AinaYaKuku)

            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)
            #ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La Chanjo.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi','Location', 'Umri Wa Kuku Kwa Siku'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.UmriWaKukuKwaSiku])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllKumbushoLaChanjo.html',context)















#-----------------------KUMBUSHO LA USAFISHAJI BANDA-----------------------


@login_required(login_url='Mylogin_user')
def AllKumbushoUsafishajiBanda(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoUsafishajiBandaSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoUsafishajiBanda.objects.all(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).order_by('-day_is_reached')

    count_wanaotumiwa = KumbushoUsafishajiBanda.objects.filter(
    		day_is_reached=True

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = KumbushoUsafishajiBandaSearchForm(request.POST or None)




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        "count_wanaotumiwa":count_wanaotumiwa,
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        #category__icontains=form['category'].value(),
        Muda = form['Muda'].value()

        

                                        
        queryset = KumbushoUsafishajiBanda.objects.filter(
                                        username__icontains=form['username'].value(),
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).order_by('-id')
        if (Muda != ''):
            queryset = KumbushoUsafishajiBanda.objects.all(
                   #Year__id__icontains = yearId.id,
                ).order_by('-id')
            queryset = queryset.filter(Muda_id=Muda)

            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)
            #ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La Usafishaji Banda.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Akumbushwe Baada Ya Siku', 'Awamu Za Kukumbushwa', 'Muda'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.SikuZaKukumbushwa, x.Awamu, x.Muda])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        "count_wanaotumiwa":count_wanaotumiwa,
        
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllKumbushoUsafishajiBanda.html',context)




@login_required(login_url='Mylogin_user')
def AllKumbushoUsafishajiBanda_ISRED(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoUsafishajiBandaSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoUsafishajiBanda.objects.filter(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,
            day_is_reached=True
            #message_is_sent=False

        ).order_by('-id')


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = KumbushoUsafishajiBandaSearchForm(request.POST or None)




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        #category__icontains=form['category'].value(),
        Muda = form['Muda'].value()

        

                                        
        queryset = KumbushoUsafishajiBanda.objects.filter(
                                        username__icontains=form['username'].value(),
                                        day_is_reached=True
                                        #message_is_sent=False
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).order_by('-id')
        if (Muda != ''):
            queryset = KumbushoUsafishajiBanda.objects.filter(
                   #Year__id__icontains = yearId.id,
                   day_is_reached=True
                   #message_is_sent=False
                ).order_by('-id')
            queryset = queryset.filter(Muda_id=Muda)

            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)
            #ZINAISHIA HAPA ZA KUSEARCH ILA CONTEXT IPO KWA CHINI
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La Usafishaji Banda.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Akumbushwe Baada Ya Siku', 'Awamu Za Kukumbushwa', 'Muda'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.SikuZaKukumbushwa, x.Awamu, x.Muda])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllKumbushoUsafishajiBanda_ISRED.html',context)



def Tuma_KumbushoUsafishajiBanda_Kwa_Wote(request):
    users = KumbushoUsafishajiBanda.objects.filter(
        day_is_reached=True
    )

    for user in users:
        SikuZaKukumbushwa = user.SikuZaKukumbushwa
        SikuZaKukumbushwaDisplayedValue = user.SikuZaKukumbushwaDisplayedValue
        Awamu = user.Awamu
        time_left = user.time_left
        username = user.username
        email = user.email

        subject = "Mfugaji Smart"
        if Awamu == 'Maramoja tu':
            message = f"Email kutoka Mfugaji Smart App. \n Hello {username}, ulisema tukukumbushe baada ya siku {SikuZaKukumbushwaDisplayedValue}, Imebaki siku {time_left} kabla  ya siku husika ya kusafisha banda, hivyo tunakukumbusha kusafisha banda kesho. \n Hautapokea tena ili kumbusho kutokana na taarifa ulizotupa kwamba ulihitaji kukumbushwa mara moja tu"
            recipient_list = [email]

            # Mark message as sent
            user.SikuZaKukumbushwa = 0
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        elif Awamu == 'Ijirudie':
            message = f"Email kutoka Mfugaji Smart App. \n Hello {username}, ulisema tukukumbushe baada ya siku {SikuZaKukumbushwa}, Imebaki siku {time_left} kabla  ya siku husika ya kusafisha banda, hivyo tunakukumbusha kusafisha banda kesho, na tutakukumbusha tena baada ya siku {SikuZaKukumbushwa} kutoka leo"
            recipient_list = [email]

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

            # Update the reminder date and reset the day_is_reached flag
            user.SikuZaKukumbushwa += user.SikuZaKukumbushwa
            user.day_is_reached = False
            user.message_is_sent = True
            user.save()


    #------------Mwanzo for Counting----------------
    # Fetch or create an EmailSendCount entry for the logged-in user
    email_count, created = EmailSendCount_KumbushoUsafishajiBanda.objects.get_or_create(
        user=request.user,
        defaults={
        'username': request.user.username, 
        'email': request.user.email,
        'Location': request.user.Location,
        'phone': request.user.phone
        
        }
    )
    
    # Increment the count
    email_count.count += 1
    email_count.save()

    # Notify the user and redirect after all emails have been sent
    messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")
    return redirect('AllKumbushoUsafishajiBanda_ISRED')



def deleteKumbushoUsafishajiBanda(request, id):
	x = KumbushoUsafishajiBanda.objects.get(id=id)
	x.delete()
	messages.success(request, f"Umefanikiwa kumfuta {x.username} aliyewahi kuweka kumbusho")
	return redirect('AllKumbushoUsafishajiBanda')






@login_required(login_url='Mylogin_user')
def All_EmailSendCount_KumbushoUsafishajiBanda(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_KumbushoUsafishajiBandaSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_KumbushoUsafishajiBanda.objects.all(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).order_by('-id')

    


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = EmailSendCount_KumbushoUsafishajiBandaSearchForm(request.POST or None)




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        

        

                                        
        queryset = EmailSendCount_KumbushoUsafishajiBanda.objects.filter(
                                        username__icontains=form['username'].value(),
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).order_by('-id')
        
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La Usafishaji Banda.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Jumla'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.count])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        
        
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/All_EmailSendCount_KumbushoUsafishajiBanda.html',context)



















#------------------------KUMBUSHO LA UATAMIAJI WA MAYAI-------------------


@login_required(login_url='Mylogin_user')
def AllKumbushoLaUatamiajiWaMayai(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoLaUatamiajiWaMayaiSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoLaUatamiajiWaMayai.objects.all(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).order_by('-day_is_reached')

    count_wanaotumiwa = KumbushoLaUatamiajiWaMayai.objects.filter(
    		day_is_reached=True

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = KumbushoLaUatamiajiWaMayaiSearchForm(request.POST or None)




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        "count_wanaotumiwa":count_wanaotumiwa,
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':

        queryset = KumbushoLaUatamiajiWaMayai.objects.filter(
                                        username__icontains=form['username'].value(),
                                        day_is_reached=True
                                        #message_is_sent=False
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).order_by('-id')
        

        

                                        
        
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La uatamiaji Wa Mayai.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Kiasi Cha Mayai', 'Mara Ya Mwisho Mayai Kuatamiwa', 'Aina Ya Ndege', 'Alama Ya Mayai', 'Namba Ya Simu Ya Mteja', 'Kifaa Anachotumia'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.KiasiChaMayai, x.SikuYaNgapiTokaKuatamiwa, x.AinaYaNdege, x.JinaLaUlipoYatoaMayai, x.NambaYakeYaSimu, x.Kifaa])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        "count_wanaotumiwa":count_wanaotumiwa,
        
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllKumbushoLaUatamiajiWaMayai.html',context)




@login_required(login_url='Mylogin_user')
def AllKumbushoLaUatamiajiWaMayai_ISRED(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoLaUatamiajiWaMayaiSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoLaUatamiajiWaMayai.objects.filter(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,
            day_is_reached=True
            #message_is_sent=False

        ).order_by('-id')


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = KumbushoLaUatamiajiWaMayaiSearchForm(request.POST or None)






    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        

        

                                        
        queryset = KumbushoLaUatamiajiWaMayai.objects.filter(
                                        username__icontains=form['username'].value(),
                                        day_is_reached=True
                                        #message_is_sent=False
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).order_by('-id')
        
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La Chanjo.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Kiasi Cha Mayai', 'Mara Ya Mwisho Mayai Kuatamiwa', 'Aina Ya Ndege', 'Alama Ya Mayai', 'Namba Ya Simu Ya Mteja', 'Kifaa Anachotumia'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.KiasiChaMayai, x.SikuYaNgapiTokaKuatamiwa, x.AinaYaNdege, x.JinaLaUlipoYatoaMayai, x.NambaYakeYaSimu, x.Kifaa])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllKumbushoLaUatamiajiWaMayai_ISRED.html',context)



def Tuma_KumbushoLaUatamiajiWaMayai_Kwa_Wote(request):
    users = KumbushoLaUatamiajiWaMayai.objects.filter(
        day_is_reached=True
    )

    for user in users:
        KiasiChaMayai = user.KiasiChaMayai
        SikuYaNgapiTokaKuatamiwa = user.SikuYaNgapiTokaKuatamiwa
        AinaYaNdege = user.AinaYaNdege
        SikuKamiliZaKuatamia = user.SikuKamiliZaKuatamia
        SikuKamiliZaKuatamiaDisplayed = user.SikuKamiliZaKuatamiaDisplayed
        JinaLaUlipoYatoaMayai = user.JinaLaUlipoYatoaMayai
        Kifaa = user.Kifaa
        phone = user.phone
        

        time_left = user.time_left
        username = user.username
        email = user.email

        subject = "Mfugaji Smart"
        if time_left == 2:
            message = f"Email kutoka Mfugaji Smart App. \n Hello {username}, leo ni siku ya kupokea kumbusho la uatamiaji wa mayai yenye hefuri (au Mteja) {JinaLaUlipoYatoaMayai} ambayo yalikuwa na siku {SikuYaNgapiTokaKuatamiwa} toka mara ya mwisho kuatamiwa kwake. \n Hivyo kesho kutwa (siku 2 baada ya leo) ndio siku ya kuatamiwa mayai yako hivyo tumekupa kumbusho leo uweze kujiandaa. \n Aina ya ndege wako {AinaYaNdege}. \n Kifaa unachotumia {Kifaa}"
            recipient_list = [email]

            # Mark message as sent
            user.SikuKamiliZaKuatamia = 0
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


    #------------Mwanzo for Counting----------------
    # Fetch or create an EmailSendCount entry for the logged-in user
    email_count, created = EmailSendCount_KumbushoLaUatamiajiWaMayai.objects.get_or_create(
        user=request.user,
        defaults={
        'username': request.user.username, 
        'email': request.user.email,
        'Location': request.user.Location,
        'phone': request.user.phone
        
        }
    )
    
    # Increment the count
    email_count.count += 1
    email_count.save()



    #----------Mwisho for Counting---------------

        


    # Notify the user and redirect after all emails have been sent
    messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")
    return redirect('AllKumbushoLaUatamiajiWaMayai_ISRED')



def deleteKumbushoLaUatamiajiWaMayai(request, id):
	x = KumbushoLaUatamiajiWaMayai.objects.get(id=id)
	x.delete()
	messages.success(request, f"Umefanikiwa kumfuta {x.username} aliyewahi kuweka kumbusho")
	return redirect('AllKumbushoLaUatamiajiWaMayai')










@login_required(login_url='Mylogin_user')
def All_EmailSendCount_KumbushoLaUatamiajiWaMayai(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_KumbushoLaUatamiajiWaMayaiSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_KumbushoLaUatamiajiWaMayai.objects.all(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).order_by('-id')

    


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = EmailSendCount_KumbushoLaUatamiajiWaMayaiSearchForm(request.POST or None)




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        

        

                                        
        queryset = EmailSendCount_KumbushoLaUatamiajiWaMayai.objects.filter(
                                        username__icontains=form['username'].value(),
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).order_by('-id')
        
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Kumbusho La Usafishaji Banda.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Jumla'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.count])
            return response
            #ZINAISHIA HAPA ZA KUDOWNLOAD

            #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
        context ={
        #"QuerySet":QuerySet,
        "form":form,
        "queryset":queryset,
        "page":page,
        
        
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/All_EmailSendCount_KumbushoLaUatamiajiWaMayai.html',context)
















@login_required(login_url='login')
def search_KumbushoLaChanjo_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = KumbushoLaChanjo.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='login')
def search_KumbushoUsafishajiBanda_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = KumbushoUsafishajiBanda.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_KumbushoLaUatamiajiWaMayai_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = KumbushoLaUatamiajiWaMayai.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='login')
def search_EmailSendCount_KumbushoLaUatamiajiWaMayai_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_KumbushoLaUatamiajiWaMayai.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='login')
def search_EmailSendCount_KumbushoUsafishajiBanda_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_KumbushoUsafishajiBanda.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

