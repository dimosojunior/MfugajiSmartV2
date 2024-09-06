# App/scheduler.py
from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from App.models import KumbushoLaChanjo
from django.core.mail import send_mail
from django.conf import settings

def weekly_vaccine_reminder():
    users = KumbushoUsafishajiBanda.objects.all()

    for item in users:
        SikuZaKukumbushwa = item.SikuZaKukumbushwa
        Awamu = item.Awamu
        username = item.username

        

        # Send an email to the user
        email = item.email
        subject = "Mfugaji Smart"
        message = f"Email kutoka Mfugaji Smart App. \n Hello {username}, leo ni siku ya kusafisha banda"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        print(f"UMRI {SikuZaKukumbushwa}")
        print(f"Jina: {username}, Siku: {SikuZaKukumbushwa}")
        print(f"ANAFUATA MWINGINE \n \n")

        # After processing, increment UmriWaKukuKwaSiku by 7 for the next run
        # item.UmriWaKuku.UmriKwaSiku += 7
        # item.UmriWaKuku.save()

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    # Pass the function object directly
    scheduler.add_job(weekly_vaccine_reminder, 'interval', seconds=5, replace_existing=True, id='weekly_vaccine_reminder')

    register_events(scheduler)
    scheduler.start()
