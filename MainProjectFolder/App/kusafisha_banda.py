import schedule
import time as tm
from django.conf import settings
from django.core.mail import send_mail
from App.models import *

# Track users who have been sent an email with 'Maramoja tu'
sent_once_users = set()

def send_email_to_user(user):
    SikuZaKukumbushwa = user.SikuZaKukumbushwa
    username = user.username
    Awamu = user.Awamu

    # If Awamu is 'Maramoja tu' and the email has already been sent, skip sending
    if Awamu == 'Maramoja tu' and user.id in sent_once_users:
        return

    print(f"Username: {username} Ukumbushwe baada ya siku {SikuZaKukumbushwa}")

    # Tuma barua pepe kwa mtumiaji
    email = user.email
    subject = "Mfugaji Smart"
    message = f"Test Kusafisha Banda : Email kutoka Mfugaji Smart App. \n Hello {username}, ulisema tukukumbushe baada ya siku {SikuZaKukumbushwa}, leo ni siku ya {SikuZaKukumbushwa} toka uweke kumbusho lako, hivyo tunakukumbusha kusafisha banda"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    # print(f"UMRI {SikuZaKukumbushwa}")
    # print(f"Jina: {username}, Siku: {SikuZaKukumbushwa}")
    # print(f"Program Ends \n \n")

    # If Awamu is 'Maramoja tu', mark this user as having been sent an email
    if Awamu == 'Maramoja tu':
        sent_once_users.add(user.id)

def start_scheduler():
    users = KumbushoUsafishajiBanda.objects.all()

    for user in users:
        SikuZaKukumbushwa = user.SikuZaKukumbushwa
        Awamu = user.Awamu

        if SikuZaKukumbushwa:  # Ensure SikuZaKukumbushwa is not None
            if Awamu == 'Ijirudie':
                schedule.every(SikuZaKukumbushwa).seconds.do(send_email_to_user, user=user)
            elif Awamu == 'Maramoja tu':
                schedule.every(SikuZaKukumbushwa).seconds.do(send_email_to_user, user=user)

    while True:
        schedule.run_pending()
        tm.sleep(1)
