from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator
from django.db.models import Count
from django.contrib import messages
from App.models import *
from MyTemplatesApp.forms import *
from django.http import HttpResponse,HttpResponseRedirect
#from datetime import datetime, timedelta
#import pyotp
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
import random
import os
from django.http import JsonResponse
from django.db.models import Q
from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
import datetime

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
#from datetime import datetime, timedelta
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

    count_wanaotumiwa = KumbushoLaChanjo.objects.filter(
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
    
    form = KumbushoLaChanjoSearchForm(request.POST or None)




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
        "count_wanaotumiwa":count_wanaotumiwa,
        #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllKumbushoLaChanjo.html',context)










@login_required(login_url='Mylogin_user')
def AllKumbushoLaChanjo_ISRED(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoLaChanjoSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoLaChanjo.objects.filter(

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
            queryset = KumbushoLaChanjo.objects.filter(
                   #Year__id__icontains = yearId.id,
                   day_is_reached=True
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

    return render(request, 'MyTemplatesApp/AllKumbushoLaChanjo_ISRED.html',context)



def Tuma_KumbushoLaChanjo_Kwa_Wote(request):
    users = KumbushoLaChanjo.objects.filter(
        day_is_reached=True
    )

    for user in users:
        AinaYaKuku = user.AinaYaKuku.AinaYaKuku
        UmriWaKukuKwaSiku = user.UmriWaKukuKwaSiku
        UmriWaKukuKwaWiki = user.UmriWaKukuKwaWiki
        time_left = user.time_left
        username = user.username
        email = user.email

        time_elapsed = (timezone.now() - user.Created).days
        print(f"Time Ellllapsedd: {time_elapsed}")

        selected_chanjo = user.AinaYaChanjo.filter(
            Kutolewa__gt=time_elapsed
        ).first()

        subject = "Mfugaji Smart"
        if selected_chanjo and time_left == 3 :
            #print("WELLLLLL")
            chanjo_name = selected_chanjo.JinaLaChanjo
            message = f"Hello {username}, leo ni siku ya kupokea kumbusho la chanjo, siku 2 baada ya leo (kesho kutwa) ndio siku ya kuku wako kupata chanjo, hivyo, unakumbushwa kuwapa kuku wako aina ya {AinaYaKuku} wenye umri wa siku {UmriWaKukuKwaSiku} chanjo ya {chanjo_name}"
            recipient_list = [email]

            # Mark message as sent
            #user.SikuZaKukumbushwa = 0
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)
            messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")

        else:
            print("BAD")
            #chanjo_name = "Hakuna Chanjo inayofaa kwa siku hii"
            messages.success(request, "Hakuna Chanjo inayofaa kwa siku hii")

        


    #------------Mwanzo for Counting----------------
    # Fetch or create an EmailSendCount entry for the logged-in user
    email_count, created = EmailSendCount_KumbushoLaChanjo.objects.get_or_create(
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
    # messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")
    return redirect('AllKumbushoLaChanjo_ISRED')



def deleteKumbushoLaChanjo(request, id):
    x = KumbushoLaChanjo.objects.get(id=id)
    x.delete()
    messages.success(request, f"Umefanikiwa kumfuta {x.username} aliyewahi kuweka kumbusho")
    return redirect('AllKumbushoLaChanjo')






@login_required(login_url='Mylogin_user')
def All_EmailSendCount_KumbushoLaChanjo(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_KumbushoLaChanjoSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_KumbushoLaChanjo.objects.all(

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
    
    form = EmailSendCount_KumbushoLaChanjoSearchForm(request.POST or None)




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
        

        

                                        
        queryset = EmailSendCount_KumbushoLaChanjo.objects.filter(
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

    return render(request, 'MyTemplatesApp/All_EmailSendCount_KumbushoLaChanjo.html',context)







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
                                        #day_is_reached=True
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






















#----------------------------KUMBUSHO LA MABADILIKO YA LISHE-----------


@login_required(login_url='Mylogin_user')
def AllKumbushoLaMabadilikoYaLishe(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoLaMabadilikoYaLisheSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoLaMabadilikoYaLishe.objects.all(

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).order_by('-day_is_reached')

    count_wanaotumiwa = KumbushoLaMabadilikoYaLishe.objects.filter(
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
    
    form = KumbushoLaMabadilikoYaLisheSearchForm(request.POST or None)




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

        queryset = KumbushoLaMabadilikoYaLishe.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
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
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Aina Ya Kuku', 'Umri Wa Kuku', 'Kundi La Kuku', 'Mfumo Anaoutumia', 'Lengo La Kufuga', 'Muda Wa Kumbusho'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.AinaYaKuku, x.UmriWaKukuKwaWiki, x.KundiLaKukuWake, x.MfumoWaKufuga, x.LengoLaKufuga, x.MudaWaKumbusho])
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

    return render(request, 'MyTemplatesApp/AllKumbushoLaMabadilikoYaLishe.html',context)




@login_required(login_url='Mylogin_user')
def AllKumbushoLaMabadilikoYaLishe_ISRED(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = KumbushoLaMabadilikoYaLisheSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = KumbushoLaMabadilikoYaLishe.objects.filter(

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
    
    form = KumbushoLaMabadilikoYaLisheSearchForm(request.POST or None)






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
        

        

                                        
        queryset = KumbushoLaMabadilikoYaLishe.objects.filter(
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
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Aina Ya Kuku', 'Umri Wa Kuku', 'Kundi La Kuku', 'Mfumo Anaoutumia', 'Lengo La Kufuga', 'Muda Wa Kumbusho'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.AinaYaKuku, x.UmriWaKukuKwaWiki, x.KundiLaKukuWake, x.MfumoWaKufuga, x.LengoLaKufuga, x.MudaWaKumbusho])
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

    return render(request, 'MyTemplatesApp/AllKumbushoLaMabadilikoYaLishe_ISRED.html',context)










def Tuma_KumbushoLaMabadilikoYaLishe_Kwa_Wote(request):
    users = KumbushoLaMabadilikoYaLishe.objects.filter(
        day_is_reached=True
    )

    for user in users:
        AinaYaKuku = user.AinaYaKuku
        # UmriWaKukuKwaSiku = user.UmriWaKukuKwaSiku
        # UmriWaKukuKwaWiki = user.UmriWaKukuKwaWiki
        UmriWaKukuKwaSiku = user.UmriWaKukuKwaSiku_KwaMahesabuTu
        UmriWaKukuKwaWiki = user.UmriWaKukuKwaWiki_KwaMahesabuTu
        KundiLaKukuWake = user.KundiLaKukuWake
        MfumoWaKufuga = user.MfumoWaKufuga
        LengoLaKufuga = user.LengoLaKufuga
        MudaWaKumbusho = user.MudaWaKumbusho

        phone = user.phone
        

        time_left = user.time_left
        username = user.username
        email = user.email

        subject = "Mfugaji Smart"

        #----------------------MWANZO WA KUKU-------------------

        #---------------KUKU WA WIKI 1----------------------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 4
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 28
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #---------------KUKU WA WIKI 2----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 21
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------------KUKU WA WIKI 3---------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 2
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 14
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #-----------------------KUKU WA WIKI 4---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 1
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 7
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #---------------KUKU WA WIKI 5------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 13 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 91
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #----------------KUKU WA WIKI 6-------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 12 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 84
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #-----------------KUKU WA WIKI 7----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 11 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 77
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #---------------KUKU WA WIKI 8-----------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 10 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 70
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #----------------KUKU WA WIKI 9-------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 9 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 63
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #--------------------KUKU WA WIKI 10---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 8 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 56
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #-------------KUKU WA WIKI 11------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 7 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 49
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #-----------KUKU WA WIKI 12-----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 6 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 42
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-------------------KUKU WA WIKI 13----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 5 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 35
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------KUKU WA WIKI 14------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 4 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 28
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------------KUKU WA WIKI 15--------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 3 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 21
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #---------------KUKU WA WIKI 16--------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 2 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 14
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------------KUKU WA WIKI 17----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku aina ya Kroila" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku wa Mayai (Layers)" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku aina ya Sasso" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku aina ya Tanbro" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119) or (AinaYaKuku == "Kuku aina ya Kenbro" and UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 1 #ili kufikia wiki ya 18
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 7
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------------------MWISHO WA KUKU-------------------------------






        #---------------------MWANZO WA KUKU MWINGINE----------------

        #-------------KUKU WA WIKI 1-----------
        if (time_left == 0) and (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 2 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 14
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #----------------KUKU WA WIKI 2-------------
        if (time_left == 0) and (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 1 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 7
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------------KUKU WA WIKI 3-------------
        if (time_left == 0) and (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Finisher feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 2 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 14
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #----------------KUKU WA WIKI 4--------------
        if (time_left == 0) and (AinaYaKuku == "Kuku aina ya Broila (kuku wa nyama)" and UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Finisher feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 1 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 7
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #-------------------------MWISHO WA KUKU-----------------


        #--------------------MWANZO WA KUKU MWINGINE--------------
        #-----------KUKU WA WIKI 1---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 0 and UmriWaKukuKwaSiku <= 7)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 6 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 42
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #----------------------KUKU WA WIKI 2-------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 8 and UmriWaKukuKwaSiku <= 14)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 5 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 35
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------------KUKU WA WIKI 3----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 15 and UmriWaKukuKwaSiku <= 21)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 4 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 28
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-------------KUKU WA WIKI 4------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 22 and UmriWaKukuKwaSiku <= 28)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 3 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 21
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------------KUKU WA WIKI 5---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 29 and UmriWaKukuKwaSiku <= 35)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 2 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 14
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #----------------KUKU WA WIKI 6---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 36 and UmriWaKukuKwaSiku <= 42)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka starter feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Grower feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 1 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 7
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #-----------------KUKU WA WIKI 7-------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 43 and UmriWaKukuKwaSiku <= 49)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 15 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 105
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-------------KUKU WA WIKI 8---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 50 and UmriWaKukuKwaSiku <= 56)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 14 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 98
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #--------------KUKU WA WIKI 9-----
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 57 and UmriWaKukuKwaSiku <= 63)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 13 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 91
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #----------------KUKU WA WIKI 10----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 64 and UmriWaKukuKwaSiku <= 70)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 12 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 84
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------KUKU WA WIKI 11----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 71 and UmriWaKukuKwaSiku <= 77)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 11 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 77
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------------KUKU WA WIKI 12---
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 78 and UmriWaKukuKwaSiku <= 84)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 10 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 70
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------KUKU WA WIKI 13--------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 85 and UmriWaKukuKwaSiku <= 91)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 9 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 63
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------------KUKU WA WIKI 14----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 92 and UmriWaKukuKwaSiku <= 98)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 8 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 56
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------KUKU WA WIKI 15--------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 99 and UmriWaKukuKwaSiku <= 105)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 7 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 49
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------KUKU WA WIKI 16--------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 106 and UmriWaKukuKwaSiku <= 112)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 6 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 42
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------------KUKU WA WIKI 17---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 113 and UmriWaKukuKwaSiku <= 119)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 5 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 35
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #------------------KUKU WA WIKI 18----------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 120 and UmriWaKukuKwaSiku <= 126)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 4 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 28
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


        #----------------KUKU WA WIKI 19---------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 127 and UmriWaKukuKwaSiku <= 133)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 127 and UmriWaKukuKwaSiku <= 133)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 3 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 21
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #-----------KUKU WA WIKI 20-------------
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 134 and UmriWaKukuKwaSiku <= 140)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 134 and UmriWaKukuKwaSiku <= 140)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 2 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 14
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)

        #------------------KUKU WA WIKI 21-----
        if (time_left == 0) and ((AinaYaKuku == "Kuku wa Malawi") and (UmriWaKukuKwaSiku >= 141 and UmriWaKukuKwaSiku <= 147)) or ((AinaYaKuku == "Kuku wa Kienyeji") and (UmriWaKukuKwaSiku >= 141 and UmriWaKukuKwaSiku <= 147)):
            message = f"Hello {username}, ndugu mfugaji smart, baada ya wiki hii, kuanzia wiki ijayo unakumbushwa kubadilisha lishe kutoka Grower feed kwa kundi la kuku waliosajiliwa kama {KundiLaKukuWake} na kuanza kutumia Layer feed mpaka pale utakapokumbushwa kubadilisha tena lishe. Ahsante. \n Aina ya kuku wako {AinaYaKuku}. \n Njia Unayotumia {MfumoWaKufuga}"
            recipient_list = [email]

            # Mark message as sent
            
            user.UmriWaKukuKwaWiki_KwaMahesabuTu += 1 #ili kufikia wiki ya 3
            user.UmriWaKukuKwaSiku_KwaMahesabuTu += 7
            user.message_is_sent = True
            user.day_is_reached = False
            user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)





    #------------Mwanzo for Counting----------------
    # Fetch or create an EmailSendCount entry for the logged-in user
    email_count, created = EmailSendCount_KumbushoLaMabadilikoYaLishe.objects.get_or_create(
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
    return redirect('AllKumbushoLaMabadilikoYaLishe_ISRED')



def deleteKumbushoLaMabadilikoYaLishe(request, id):
    x = KumbushoLaMabadilikoYaLishe.objects.get(id=id)
    x.delete()
    messages.success(request, f"Umefanikiwa kumfuta {x.username} aliyewahi kuweka kumbusho")
    return redirect('AllKumbushoLaMabadilikoYaLishe')










@login_required(login_url='Mylogin_user')
def All_EmailSendCount_KumbushoLaMabadilikoYaLishe(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_KumbushoLaMabadilikoYaLisheSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_KumbushoLaMabadilikoYaLishe.objects.all(

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
    
    form = EmailSendCount_KumbushoLaMabadilikoYaLisheSearchForm(request.POST or None)




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
        

        

                                        
        queryset = EmailSendCount_KumbushoLaMabadilikoYaLishe.objects.filter(
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

    return render(request, 'MyTemplatesApp/All_EmailSendCount_KumbushoLaMabadilikoYaLishe.html',context)


























#-------------------------DUKA LAKO------------------------

@login_required(login_url='Mylogin_user')
def AllDukaLako(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = DukaLakoSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = DukaLako.objects.filter(

            Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,

        ).order_by('-id')

    count_wanaotumiwa = DukaLako.objects.all(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).exclude(Status__Status__in=["Approved"]).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = DukaLakoSearchForm(request.POST or None)




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

        queryset = DukaLako.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
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
            response['content-Disposition'] = 'attachment; filename="Duka Lako.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Title', 'Maelezo', 'Kampuni Yake', 'Tick Status'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.Title, x.Maelezo, x.company_name, x.TickStatus])
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

    return render(request, 'MyTemplatesApp/AllDukaLako.html',context)




def DukaLakoDetailPage(request, id):
    queryset = DukaLako.objects.get(id=id)

    form = DukaLakoUpdateForm(instance=queryset)
    if request.method == "POST":
        # Title = request.POST.get('Title')
        form = DukaLakoUpdateForm(request.POST, files=request.FILES, instance=queryset)

        if form.is_valid():
            form.save()

            #send Email
            subject = "Mfugaji Smart"
            message = f"Hongera {queryset.username}, Mfugaji Smart inakutaarifu kuwa posti yako ya {queryset.Title} yenye maelezo haya {queryset.Maelezo}, imehakikiwa na kukidhi vigezo vyote. \n Sasa ipo ndani ya programu yetu ya Mfugaji Smart"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [queryset.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            #------------Mwanzo for Counting----------------
            # Fetch or create an EmailSendCount entry for the logged-in user
            email_count, created = EmailSendCount_DukaLako.objects.get_or_create(
                user=request.user,
                defaults={
                'username': request.user.username, 
                'email': request.user.email,
                'Location': request.user.Location,
                'phone': request.user.phone,
                'ApprovedPost': queryset.Title,
                'ApprovedMaelezoPost': queryset.Maelezo,
                
                }
            )
            
            # Increment the count
            email_count.count += 1
            email_count.save()

            messages.success(request, f"Posti ya  {queryset.username}, {queryset.Title} imehakikiwa kikamilifu")
            return redirect('AllPendingPostiDukaLako')



        messages.success(request, f"Kuna tatizo kwenye kuhakiki taarifa za {queryset.username}")
        return redirect('DukaLakoDetailPage', id=id)
    
    context ={
        
        "queryset":queryset,
        "form":form,
    }
    
    
        

    return render(request, 'MyTemplatesApp/DukaLakoDetailPage.html',context)

def HakikiDukaLako(request,id):
    x = DukaLako.objects.get(id=id)
    form = DukaLakoUpdateForm(instance=x)
    if request.method == "POST":
        # Title = request.POST.get('Title')
        form = DukaLakoUpdateForm(request.POST, files=request.FILES, instance=x)

        if form.is_valid():
            form.save()
            messages.success(request, f"Posti ya  {x.username}, {x.Title} imehakikiwa kikamilifu")
            return redirect('AllPendingPostiDukaLako')

        messages.success(request, f"Kuna tatizo kwenye kuhakiki taarifa za {x.username}")
        return redirect('HakikiDukaLako', id=id)


    context ={
        
        "form":form,
        
    }
    
    
        

    return render(request, 'MyTemplatesApp/HakikiDukaLako.html',context)



def deleteDukaLako(request, id):
    x = DukaLako.objects.get(id=id)
    x.delete()
    messages.success(request, f"Umefanikiwa kumfuta {x.username}")
    return redirect('AllDukaLako')


@login_required(login_url='Mylogin_user')
def AllPendingPostiDukaLako(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = DukaLakoSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = DukaLako.objects.all(

            #Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,

        ).exclude(Status__Status__in=["Approved"]).order_by('-id')

    count_wanaotumiwa = DukaLako.objects.all(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).exclude(Status__Status__in=["Approved"]).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = DukaLakoSearchForm(request.POST or None)




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

        queryset = DukaLako.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
                                        #message_is_sent=False
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).exclude(Status__Status__in=["Approved"]).order_by('-id')
        

        

                                        
        
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Duka Lako.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Title', 'Maelezo', 'Kampuni Yake', 'Tick Status'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.Title, x.Maelezo, x.company_name, x.TickStatus])
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

    return render(request, 'MyTemplatesApp/AllPendingPostiDukaLako.html',context)









@login_required(login_url='Mylogin_user')
def All_EmailSendCount_DukaLako(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_DukaLakoSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_DukaLako.objects.all(

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
    
    form = EmailSendCount_DukaLakoSearchForm(request.POST or None)




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
        username = form['username'].value()
        startDate = form['start_date'].value()
        endDate = form['end_date'].value()

        if (username != '' and startDate == '' and endDate == ''):
                                                
            queryset = EmailSendCount_DukaLako.objects.filter(
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

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        if (username == '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                                                
            queryset = EmailSendCount_DukaLako.objects.filter(
                                            last_sent__gte=start_date, 
                                            last_sent__lte=end_date,
                                            #username__icontains=form['username'].value(),
                                            # Class__id__icontains = classId_id,
                                            # Year__id__icontains = yearId.id,

                                            #last_updated__gte=form['start_date'].value(),
                                            # last_updated__lte=form['end_date'].value()
                                            #last_updated__range=[
                                                #form['start_date'].value(),
                                                #form['end_date'].value()
                                            #]
                ).order_by('-id')

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        if (username != '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                                                
            queryset = EmailSendCount_DukaLako.objects.filter(
                                            last_sent__gte=start_date, 
                                            last_sent__lte=end_date,
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

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)



        
        
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

    return render(request, 'MyTemplatesApp/All_EmailSendCount_DukaLako.html',context)





























#-------------------------MY USERS---------------------------


@login_required(login_url='Mylogin_user')
def AllMyUser(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = MyUserSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = MyUser.objects.filter(

            #Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,
            Tick__icontains="Ndio Anastahili"

        ).order_by('-id')

    count_wanaotumiwa = MyUser.objects.all(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).exclude(Tick__in=["Ndio Anastahili"]).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = MyUserSearchForm(request.POST or None)




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

        queryset = MyUser.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
                                        Tick__icontains="Ndio Anastahili",
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
            response['content-Disposition'] = 'attachment; filename="Duka Lako.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Title', 'Maelezo', 'Kampuni Yake','Mkoa', 'Tick Status', 'Siku Aliyojisajili'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.Title, x.Maelezo, x.company_name, x.Mkoa.JinaLaMkoa, x.TickStatus, x.date_joined])
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

    return render(request, 'MyTemplatesApp/AllMyUser.html',context)




def MyUserDetailPage(request, id):
    queryset = MyUser.objects.get(id=id)

    form = MyUserUpdateForm(instance=queryset)
    if request.method == "POST":
        # Title = request.POST.get('Title')
        form = MyUserUpdateForm(request.POST, files=request.FILES, instance=queryset)

        if form.is_valid():
            form.save()

            #send Email
            subject = "Mfugaji Smart"
            message = f"Hongera {queryset.username}, Mfugaji Smart inakutaarifu kuwa ombi lako la kuomba kuidhinishwa limepitiwa na kukubaliwa. \n Endelea kutumia programu yetu ya Mfugaji Smart kupata huduma nzuri na bora zaidi"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [queryset.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            #------------Mwanzo for Counting----------------
            # Fetch or create an EmailSendCount entry for the logged-in user
            email_count, created = EmailSendCount_MyUser.objects.get_or_create(
                user=request.user,
                defaults={
                'username': request.user.username, 
                'email': request.user.email,
                'Location': request.user.Location,
                'phone': request.user.phone,
                'ApprovedUser': queryset.username,
                'ApprovedMaelezoUser': queryset.Maelezo,
                
                }
            )
            
            # Increment the count
            email_count.count += 1
            email_count.save()

            messages.success(request, f"Taarifa ya  {queryset.username}, zimehidhinishwa kikamilifu")
            return redirect('AllPendingMyUser')



        messages.success(request, f"Kuna tatizo kwenye kuhakiki taarifa za {queryset.username}")
        return redirect('MyUserDetailPage', id=id)
    
    context ={
        
        "queryset":queryset,
        "form":form,
    }
    
    
        

    return render(request, 'MyTemplatesApp/MyUserDetailPage.html',context)

def HakikiMyUser(request,id):
    x = MyUser.objects.get(id=id)
    form = MyUserUpdateForm(instance=x)
    if request.method == "POST":
        # Title = request.POST.get('Title')
        form = MyUserUpdateForm(request.POST, files=request.FILES, instance=x)

        if form.is_valid():
            form.save()
            messages.success(request, f"Posti ya  {x.username}, {x.Title} imehakikiwa kikamilifu")
            return redirect('AllPendingPostiMyUser')

        messages.success(request, f"Kuna tatizo kwenye kuhakiki taarifa za {x.username}")
        return redirect('HakikiMyUser', id=id)


    context ={
        
        "form":form,
        
    }
    
    
        

    return render(request, 'MyTemplatesApp/HakikiMyUser.html',context)



def deleteMyUser(request, id):
    x = MyUser.objects.get(id=id)
    x.delete()
    messages.success(request, f"Umefanikiwa kumfuta {x.username} ")
    return redirect('AllMyUser')


@login_required(login_url='Mylogin_user')
def AllPendingMyUser(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = MyUserSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = MyUser.objects.all(

            #Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,

        ).exclude(Tick__in=["Ndio Anastahili"]).order_by('-id')

    count_wanaotumiwa = MyUser.objects.all(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,

        ).exclude(Tick__in=["Ndio Anastahili"]).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,10)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = MyUserSearchForm(request.POST or None)




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

        queryset = MyUser.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
                                        #message_is_sent=False
                                        # Class__id__icontains = classId_id,
                                        # Year__id__icontains = yearId.id,

                                        #last_updated__gte=form['start_date'].value(),
                                        # last_updated__lte=form['end_date'].value()
                                        #last_updated__range=[
                                            #form['start_date'].value(),
                                            #form['end_date'].value()
                                        #]
            ).exclude(Tick__in=["Ndio Anastahili"]).order_by('-id')
        

        

                                        
        
        
        #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
        if form['export_to_CSV'].value() == True:
            response = HttpResponse(content_type='text/csv')
            response['content-Disposition'] = 'attachment; filename="Duka Lako.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Anapoishi', 'Title', 'Maelezo', 'Kampuni Yake','Mkoa', 'Tick Status', 'Siku Aliyojisajili'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.Title, x.Maelezo, x.company_name, x.Mkoa.JinaLaMkoa, x.TickStatus, x.date_joined])
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

    return render(request, 'MyTemplatesApp/AllPendingMyUser.html',context)









@login_required(login_url='Mylogin_user')
def All_EmailSendCount_MyUser(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_MyUserSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_MyUser.objects.all(

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
    
    form = EmailSendCount_MyUserSearchForm(request.POST or None)




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
        username = form['username'].value()
        startDate = form['start_date'].value()
        endDate = form['end_date'].value()

        if (username != '' and startDate == '' and endDate == ''):
                                                
            queryset = EmailSendCount_MyUser.objects.filter(
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

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        if (username == '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                                                
            queryset = EmailSendCount_MyUser.objects.filter(
                                            last_sent__gte=start_date, 
                                            last_sent__lte=end_date,
                                            #username__icontains=form['username'].value(),
                                            # Class__id__icontains = classId_id,
                                            # Year__id__icontains = yearId.id,

                                            #last_updated__gte=form['start_date'].value(),
                                            # last_updated__lte=form['end_date'].value()
                                            #last_updated__range=[
                                                #form['start_date'].value(),
                                                #form['end_date'].value()
                                            #]
                ).order_by('-id')

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        if (username != '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                                                
            queryset = EmailSendCount_MyUser.objects.filter(
                                            last_sent__gte=start_date, 
                                            last_sent__lte=end_date,
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

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)



        
        
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

    return render(request, 'MyTemplatesApp/All_EmailSendCount_MyUser.html',context)












#----------------------MAONI----------------------

@login_required(login_url='Mylogin_user')
def AllMaoni(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = MaoniSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = Maoni.objects.filter(

            #Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,
            is_checked = True
            

        ).order_by('-id')

    count_wanaotumiwa = Maoni.objects.filter(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,
            is_checked = False

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
    
    form = MaoniSearchForm(request.POST or None)




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

        queryset = Maoni.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
                                        is_checked = True
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
            response['content-Disposition'] = 'attachment; filename="Maoni.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Maoni', 'Je Yamefanyiwa Kazi', 'Siku Yaliyotolewa'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.Maoni, x.is_checked, x.Created])
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

    return render(request, 'MyTemplatesApp/AllMaoni.html',context)






@login_required(login_url='Mylogin_user')
def AllPendingMaoni(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = MaoniSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = Maoni.objects.filter(

            #Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,
            is_checked = False
            

        ).order_by('-id')

    count_wanaotumiwa = Maoni.objects.filter(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,
            is_checked = False

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
    
    form = MaoniSearchForm(request.POST or None)




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

        queryset = Maoni.objects.filter(
                                        username__icontains=form['username'].value(),
                                        #day_is_reached=True
                                        is_checked = False
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
            response['content-Disposition'] = 'attachment; filename="Maoni.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina Kamili','Email', 'Namba Ya Simu', 'Maoni', 'Je Yamefanyiwa Kazi', 'Siku Yaliyotolewa'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.username,x.email,x.phone, x.Location,x.Maoni, x.is_checked, x.Created])
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

    return render(request, 'MyTemplatesApp/AllPendingMaoni.html',context)














@login_required(login_url='Mylogin_user')
def All_EmailSendCount_Maoni(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = EmailSendCount_MaoniSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = EmailSendCount_Maoni.objects.all(

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
    
    form = EmailSendCount_MaoniSearchForm(request.POST or None)




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
        username = form['username'].value()
        startDate = form['start_date'].value()
        endDate = form['end_date'].value()

        if (username != '' and startDate == '' and endDate == ''):
                                                
            queryset = EmailSendCount_Maoni.objects.filter(
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

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        if (username == '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                                                
            queryset = EmailSendCount_Maoni.objects.filter(
                                            last_sent__gte=start_date, 
                                            last_sent__lte=end_date,
                                            #username__icontains=form['username'].value(),
                                            # Class__id__icontains = classId_id,
                                            # Year__id__icontains = yearId.id,

                                            #last_updated__gte=form['start_date'].value(),
                                            # last_updated__lte=form['end_date'].value()
                                            #last_updated__range=[
                                                #form['start_date'].value(),
                                                #form['end_date'].value()
                                            #]
                ).order_by('-id')

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)

        if (username != '' and startDate != '' and endDate != ''):
            start_date = request.POST.get('start_date')
            end_date = request.POST.get('end_date')

            # Adjust the date range by adding one day to the end date
            end_date = datetime.datetime.strptime(end_date, '%Y-%m-%d') + datetime.timedelta(days=1)
                                                
            queryset = EmailSendCount_Maoni.objects.filter(
                                            last_sent__gte=start_date, 
                                            last_sent__lte=end_date,
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

        paginator = Paginator(queryset, 10)  # Show 6 contacts per page
        page = request.GET.get('page')
        queryset = paginator.get_page(page)



        
        
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

    return render(request, 'MyTemplatesApp/All_EmailSendCount_Maoni.html',context)






def MaoniDetailPage(request, id):
    queryset = Maoni.objects.get(id=id)

    form = MaoniUpdateForm(instance=queryset)
    if request.method == "POST":
        # Title = request.POST.get('Title')
        form = MaoniUpdateForm(request.POST, files=request.FILES, instance=queryset)

        if form.is_valid():
            form.save()

            #send Email
            subject = "Mfugaji Smart"
            message = f"Hongera {queryset.username}, Mfugaji Smart inakutaarifu kuwa maoni yako yamepokelewa na yamefanyiwa kazi kikamilifu \n Endelea kutumia programu yetu ya Mfugaji Smart kupata huduma nzuri na bora zaidi"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [queryset.email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            #------------Mwanzo for Counting----------------
            # Fetch or create an EmailSendCount entry for the logged-in user
            email_count, created = EmailSendCount_Maoni.objects.get_or_create(
                user=request.user,
                defaults={
                'username': request.user.username, 
                'email': request.user.email,
                'Location': request.user.Location,
                'phone': request.user.phone,
                'ApprovedUser': queryset.username,
                'ApprovedMaelezoUser': queryset.Maoni,
                
                }
            )
            
            # Increment the count
            email_count.count += 1
            email_count.save()

            messages.success(request, f"Maoni ya  {queryset.username}, yamehakikiwa na kufanyiwa kazi kikamilifu")
            return redirect('AllPendingMaoni')



        messages.success(request, f"Kuna tatizo kwenye kuhakiki maoni ya {queryset.username}")
        return redirect('MaoniDetailPage', id=id)
    
    context ={
        
        "queryset":queryset,
        "form":form,
    }
    
    
        

    return render(request, 'MyTemplatesApp/MaoniDetailPage.html',context)

def HakikiMaoni(request,id):
    x = Maoni.objects.get(id=id)
    form = MaoniUpdateForm(instance=x)
    if request.method == "POST":
        # Title = request.POST.get('Title')
        form = MaoniUpdateForm(request.POST, files=request.FILES, instance=x)

        if form.is_valid():
            form.save()
            messages.success(request, f"Posti ya  {x.username}, {x.Title} imehakikiwa kikamilifu")
            return redirect('AllPendingPostiMaoni')

        messages.success(request, f"Kuna tatizo kwenye kuhakiki taarifa za {x.username}")
        return redirect('HakikiMaoni', id=id)


    context ={
        
        "form":form,
        
    }
    
    
        

    return render(request, 'MyTemplatesApp/HakikiMaoni.html',context)



def deleteMaoni(request, id):
    x = Maoni.objects.get(id=id)
    x.delete()
    messages.success(request, f"Umefanikiwa kufuta maoni ya {x.username} ")
    return redirect('AllMaoni')






@login_required(login_url='login')
def search_Wanunuzi_username_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = Wanunuzi.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_Wanunuzi_wilaya_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(Wilaya__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = Wanunuzi.objects.filter(search)
    mylist= []
    mylist += [x.Wilaya for x in filters]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='login')
def search_Maoni_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = Maoni.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_MyUser_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = MyUser.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_DukaLako_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = DukaLako.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_Mikoa_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(JinaLaMkoa__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = Mikoa.objects.filter(search)
    mylist= []
    mylist += [x.JinaLaMkoa for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_KumbushoLaMabadilikoYaLishe_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = KumbushoLaMabadilikoYaLishe.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)


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
def search_EmailSendCount_Maoni_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_Maoni.objects.filter(search)
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

@login_required(login_url='login')
def search_EmailSendCount_KumbushoLaMabadilikoYaLishe_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_KumbushoLaMabadilikoYaLishe.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='login')
def search_EmailSendCount_KumbushoLaChanjo_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_KumbushoLaChanjo.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)

@login_required(login_url='login')
def search_EmailSendCount_DukaLako_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_DukaLako.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)


@login_required(login_url='login')
def search_EmailSendCount_MyUser_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(username__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    filters = EmailSendCount_MyUser.objects.filter(search)
    mylist= []
    mylist += [x.username for x in filters]
    return JsonResponse(mylist, safe=False)















#-----------------------WANUNUZI-----------------------------

@login_required(login_url='Mylogin_user')
def AllMikoa(request):
    # classId_id = request.session.get('classId_id', '')
    # classId_name = request.session.get('classId_name', '')


    # classId = Classes.objects.get(id=id)
    #className = classId_name

    # yearId = Years.objects.get(id=id)
    # yearName = yearId.Year

    

    form = MikoaSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    queryset = Mikoa.objects.all(

            #Status__Status__icontains='Approved'
            # Year__id__icontains = yearId.id,
            #is_checked = True
            

        ).order_by('-id')

    count_wanaotumiwa = Mikoa.objects.all(
            #Status__Status__icontains='Approved'

            # Class__id__icontains = classId_id,
            # Year__id__icontains = yearId.id,
            #is_checked = False

        ).count()


    
    #To SET  PAGINATION IN STOCK LIST PAGE
    paginator = Paginator(queryset,6)
    page = request.GET.get('page')
    try:
        queryset=paginator.page(page)
    except PageNotAnInteger:
        queryset=paginator.page(1)
    except EmptyPage:
        queryset=paginator.page(paginator.num_pages)
    
    form = MikoaSearchForm(request.POST or None)




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

        queryset = Mikoa.objects.filter(
                                        JinaLaMkoa__icontains=form['JinaLaMkoa'].value(),
                                        #day_is_reached=True
                                        #is_checked = True
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
            response['content-Disposition'] = 'attachment; filename="Mikoa.csv"'
            writer = csv.writer(response)
            writer.writerow(['Jina La Mkoa','Kanda', 'Siku Uliosajiliwa'])
            instance = queryset
            for x in queryset:
                writer.writerow([x.JinaLaMkoa,x.Kanda, x.Created])
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

    return render(request, 'MyTemplatesApp/AllMikoa.html',context)








@login_required(login_url='Mylogin_user')
def AllWanunuzi(request,id):
    MkoaGET = Mikoa.objects.get(id=id)
    MkoaID = MkoaGET.id
    MkoaName = MkoaGET.JinaLaMkoa

    request.session['MkoaID'] = MkoaID
    request.session['MkoaName'] = MkoaName

    queryset = Wanunuzi.objects.filter(

        Mkoa__id__icontains=MkoaID

    ).order_by('-id')

    

    form = WanunuziSearchForm(request.POST or None)
    # x= datetime.now()
    # current_date = x.strftime('%d-%m-%Y %H:%M')
    

    

    count_wanaotumiwa = Wanunuzi.objects.filter(
            Mkoa__id__icontains=MkoaID

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
    
    




    #MWISHO HAP




    context ={
        "queryset":queryset,
        "form":form,
        "page":page,
        "count_wanaotumiwa":count_wanaotumiwa,
        "MkoaName":MkoaName,
        
        # "current_date":current_date,
        #"className":className,
    }

    #kwa ajili ya kufilter items and category ktk form
    if request.method == 'POST':
        username = form['username'].value()
        Wilaya = form['Wilaya'].value()
        Message = request.POST.get('Message')
        # startDate = form['start_date'].value()
        # endDate = form['end_date'].value()
        if (username == '' and Wilaya == ''):


            queryset = Wanunuzi.objects.filter(
                                            #username__icontains=form['username'].value(),
                                            Mkoa__id__icontains=MkoaID
                                            #day_is_reached=True
                                            #is_checked = True
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

            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)


            #------------------SEND EMail--------------
            Message = request.POST.get('Message')
            # print(f"MESSAGE: {Message}")
            # print(f"MkoaID: {MkoaID}")
            # print(f"MkoaName: {MkoaName}")

            for user in queryset:
                Message = Message
                username = user.username
                Mkoa = user.Mkoa.JinaLaMkoa
                phone = user.phone
                email = user.email
                Wilaya = user.Wilaya
                

                subject = "Mfugaji Smart"
                
                message = f"Hello {username}, Mfugaji Smart inakutaarifu {username} kutoka mkoa wa {Mkoa} wilaya ya {Wilaya} . \n {Message}"
                recipient_list = [email]

                # Mark message as sent
                # user.SikuKamiliZaKuatamia = 0
                # user.message_is_sent = True
                # user.day_is_reached = False
                # user.save()

                # Send email
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)
            messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")

            #------------Mwanzo for Counting----------------
            # Fetch or create an EmailSendCount entry for the logged-in user
            HistoriaZaJumbeZaWanunuzi.objects.create(
                # user=request.user,          
                # username= request.user.username, 
                # email= request.user.email,
                # Location= request.user.Location,
                # phone= request.user.phone,
                JinaLaMnunuzi=user.username,
                NambaYaSimuYaMnunuzi=user.phone,
                Mkoa=user.Mkoa.JinaLaMkoa,
                Wilaya=user.Wilaya
                
                
            )

            #------------------MWISHO WA KUSEND EMAIL-----------

        if (username != '' and Wilaya == ''):


            queryset = Wanunuzi.objects.filter(
                                            username__icontains=form['username'].value(),
                                            Mkoa__id__icontains=MkoaID
                                            #day_is_reached=True
                                            #is_checked = True
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

            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)


            #------------------SEND EMail--------------
            Message = request.POST.get('Message')
            # print(f"MESSAGE: {Message}")
            # print(f"MkoaID: {MkoaID}")
            # print(f"MkoaName: {MkoaName}")

            for user in queryset:
                Message = Message
                username = user.username
                Mkoa = user.Mkoa.JinaLaMkoa
                phone = user.phone
                email = user.email
                Wilaya = user.Wilaya
                

                subject = "Mfugaji Smart"
                
                message = f"Hello {username}, Mfugaji Smart inakutaarifu {username} kutoka mkoa wa {Mkoa} wilaya ya {Wilaya} . \n {Message}"
                recipient_list = [email]

                # Mark message as sent
                # user.SikuKamiliZaKuatamia = 0
                # user.message_is_sent = True
                # user.day_is_reached = False
                # user.save()

                # Send email
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)
                messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")

                #------------Mwanzo for Counting----------------
                # Fetch or create an EmailSendCount entry for the logged-in user
                HistoriaZaJumbeZaWanunuzi.objects.create(
                    # user=request.user,          
                    # username= request.user.username, 
                    # email= request.user.email,
                    # Location= request.user.Location,
                    # phone= request.user.phone,
                    JinaLaMnunuzi=user.username,
                    NambaYaSimuYaMnunuzi=user.phone,
                    Mkoa=user.Mkoa.JinaLaMkoa,
                    Wilaya=user.Wilaya
                    
                    
                )

            #------------------MWISHO WA KUSEND EMAIL-----------

        if (username == '' and Wilaya != ''): 

            queryset = Wanunuzi.objects.filter(
                                            Wilaya__icontains=form['Wilaya'].value(),
                                            Mkoa__id__icontains=MkoaID
                                            #day_is_reached=True
                                            #is_checked = True
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

            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)

            Message = request.POST.get('Message')
            # print(f"MESSAGE: {Message}")
            # print(f"MkoaID: {MkoaID}")
            # print(f"MkoaName: {MkoaName}")

            for user in queryset:
                Message = Message
                username = user.username
                Mkoa = user.Mkoa.JinaLaMkoa
                phone = user.phone
                email = user.email
                Wilaya = user.Wilaya
                

                subject = "Mfugaji Smart"
                
                message = f"Hello {username}, Mfugaji Smart inakutaarifu {username} kutoka mkoa wa {Mkoa} wilaya ya {Wilaya} . \n {Message}"
                recipient_list = [email]

                # Mark message as sent
                # user.SikuKamiliZaKuatamia = 0
                # user.message_is_sent = True
                # user.day_is_reached = False
                # user.save()

                # Send email
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)
                messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")

                #------------Mwanzo for Counting----------------
                # Fetch or create an EmailSendCount entry for the logged-in user
                HistoriaZaJumbeZaWanunuzi.objects.create(
                    # user=request.user,          
                    # username= request.user.username, 
                    # email= request.user.email,
                    # Location= request.user.Location,
                    # phone= request.user.phone,
                    JinaLaMnunuzi=user.username,
                    NambaYaSimuYaMnunuzi=user.phone,
                    Mkoa=user.Mkoa.JinaLaMkoa,
                    Wilaya=user.Wilaya
                    
                    
                )

            #------------------MWISHO WA KUSEND EMAIL-----------

        if (username != '' and Wilaya != ''): 

            queryset = Wanunuzi.objects.filter(
                                            username__icontains=form['username'].value(),
                                            Wilaya__icontains=form['Wilaya'].value(),
                                            Mkoa__id__icontains=MkoaID
                                            #day_is_reached=True
                                            #is_checked = True
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



            #To SET  PAGINATION IN STOCK LIST PAGE
            paginator = Paginator(queryset,10)
            page = request.GET.get('page')
            try:
                queryset=paginator.page(page)
            except PageNotAnInteger:
                queryset=paginator.page(1)
            except EmptyPage:
                queryset=paginator.page(paginator.num_pages)


            Message = request.POST.get('Message')
            # print(f"MESSAGE: {Message}")
            # print(f"MkoaID: {MkoaID}")
            # print(f"MkoaName: {MkoaName}")

            for user in queryset:
                Message = Message
                username = user.username
                Mkoa = user.Mkoa.JinaLaMkoa
                phone = user.phone
                email = user.email
                Wilaya = user.Wilaya
                

                subject = "Mfugaji Smart"
                
                message = f"Hello {username}, Mfugaji Smart inakutaarifu {username} kutoka mkoa wa {Mkoa} wilaya ya {Wilaya} . \n {Message}"
                recipient_list = [email]

                # Mark message as sent
                # user.SikuKamiliZaKuatamia = 0
                # user.message_is_sent = True
                # user.day_is_reached = False
                # user.save()

                # Send email
                send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)
                messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")

                #------------Mwanzo for Counting----------------
                # Fetch or create an EmailSendCount entry for the logged-in user
                HistoriaZaJumbeZaWanunuzi.objects.create(
                    # user=request.user,          
                    # username= request.user.username, 
                    # email= request.user.email,
                    # Location= request.user.Location,
                    # phone= request.user.phone,
                    JinaLaMnunuzi=user.username,
                    NambaYaSimuYaMnunuzi=user.phone,
                    Mkoa=user.Mkoa.JinaLaMkoa,
                    Wilaya=user.Wilaya
                    
                    
                )

            #------------------MWISHO WA KUSEND EMAIL-----------
        

        

                                        
        
        
    #hii ni kwa ajili ya kudownload ile page nzima ya stock endapo mtu akiweka tiki kwenye field export to csv
    if form['export_to_CSV'].value() == True:
        response = HttpResponse(content_type='text/csv')
        response['content-Disposition'] = 'attachment; filename="Wanunuzi.csv"'
        writer = csv.writer(response)
        writer.writerow(['Jina Kamili','Namba Ya Simu', 'Email','Mkoa', 'Wilaya', 'Siku Uliyomsajili'])
        instance = queryset
        for x in queryset:
            writer.writerow([x.username,x.phone,x.email,x.Mkoa.JinaLaMkoa, x.Wilaya, x.Created])
        return response
        #ZINAISHIA HAPA ZA KUDOWNLOAD

    #HII NI CONTEXT KWA AJILI YA KUSEARCH ITEM OR CATEGORY KWENYE FORMYETU
    context ={
    #"QuerySet":QuerySet,
    "form":form,
    "queryset":queryset,
    "page":page,
    "count_wanaotumiwa":count_wanaotumiwa,
    "MkoaName":MkoaName,
    
    #"className":className,
    }   

    return render(request, 'MyTemplatesApp/AllWanunuzi.html',context)








def Tuma_Wanunuzi_Kwa_Wote(request):
    MkoaID = request.session.get('MkoaID', '')
    MkoaName = request.session.get('MkoaName', '')

    queryset = Wanunuzi.objects.filter(
        Mkoa__id__icontains=MkoaID
    )

    #if (username != '' and Wilaya != ''): 
    
    if request.method == "POST":
        Message = request.POST.get('Message')
        # print(f"MESSAGE: {Message}")
        # print(f"MkoaID: {MkoaID}")
        # print(f"MkoaName: {MkoaName}")

        for user in queryset:
            Message = Message
            username = user.username
            Mkoa = user.Mkoa.JinaLaMkoa
            phone = user.phone
            email = user.email
            Wilaya = user.Wilaya
            

            subject = "Mfugaji Smart"
            
            message = f"Hello {username}, Mfugaji Smart inakutaarifu {username} kutoka mkoa wa {Mkoa} wilaya ya {Wilaya} . \n {Message}"
            recipient_list = [email]

            # Mark message as sent
            # user.SikuKamiliZaKuatamia = 0
            # user.message_is_sent = True
            # user.day_is_reached = False
            # user.save()

            # Send email
            send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list, fail_silently=True)


            #------------Mwanzo for Counting----------------
            # Fetch or create an EmailSendCount entry for the logged-in user
            HistoriaZaJumbeZaWanunuzi.objects.create(
                # user=request.user,          
                # username= request.user.username, 
                # email= request.user.email,
                # Location= request.user.Location,
                # phone= request.user.phone,
                JinaLaMnunuzi=user.username,
                NambaYaSimuYaMnunuzi=user.phone,
                Mkoa=user.Mkoa.JinaLaMkoa,
                Wilaya=user.Wilaya
                
                
            )
            
            



    #----------Mwisho for Counting---------------

        


    # Notify the user and redirect after all emails have been sent
    messages.success(request, "Ujumbe umetumwa kikamilivu kwa wahusika")
    return redirect('AllWanunuzi', MkoaID)

