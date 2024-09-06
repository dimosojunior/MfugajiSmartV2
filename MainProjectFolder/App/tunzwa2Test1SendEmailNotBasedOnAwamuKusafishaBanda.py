import schedule
import time as tm
from django.conf import settings
from django.core.mail import send_mail
from App.models import *

def send_email_to_user(user):
    SikuZaKukumbushwa = user.SikuZaKukumbushwa
    username = user.username

    print(f"Username: {username} Ukumbushwe baada ya siku {SikuZaKukumbushwa}")

    # Tuma barua pepe kwa mtumiaji
    email = user.email
    subject = "Mfugaji Smart"
    message = f"Kusafisha Banda : Email kutoka Mfugaji Smart App. \n Hello {username}, ulisema tukukumbushe baada ya siku {SikuZaKukumbushwa}, leo ni siku ya {SikuZaKukumbushwa} toka uweke kumbusho lako, hivyo tunakukumbusha kusafisha banda"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    # print(f"UMRI {SikuZaKukumbushwa}")
    # print(f"Jina: {username}, Siku: {SikuZaKukumbushwa}")
    # print(f"Program Ends \n \n")

def start_scheduler():
    users = KumbushoUsafishajiBanda.objects.all()

    for user in users:
        SikuZaKukumbushwa = user.SikuZaKukumbushwa
        if SikuZaKukumbushwa:  # Ensure SikuZaKukumbushwa is not None
            schedule.every(SikuZaKukumbushwa).seconds.do(send_email_to_user, user=user)

    while True:
        schedule.run_pending()
        tm.sleep(1)
