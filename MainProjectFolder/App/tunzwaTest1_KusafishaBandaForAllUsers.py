import schedule
import time as tm
from django.conf import settings
from django.core.mail import send_mail
from App.models import *

def job():
    print("Program starting here")
    users = KumbushoUsafishajiBanda.objects.all()

    for item in users:
        SikuZaKukumbushwa = item.SikuZaKukumbushwa
        Awamu = item.Awamu
        username = item.username

        print(f"Username: {username} Ukumbushwe baada ya siku {SikuZaKukumbushwa}")

        # Tuma barua pepe kwa mtumiaji
        email = item.email
        subject = "Mfugaji Smart"
        message = f"Kusafisha Banda : Email kutoka Mfugaji Smart App. \n Hello {username}, ulisema tukukumbushe baada ya siku {SikuZaKukumbushwa}, leo ni siku ya {SikuZaKukumbushwa} toka uweke kumbusho lako, hivyo tunakukumbusha kusafisha banda"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        print(f"UMRI {SikuZaKukumbushwa}")
        print(f"Jina: {username}, Siku: {SikuZaKukumbushwa}")
        print(f"Program Ends \n \n")

# Pata thamani ya dynamic variable
def start_scheduler():
    users = KumbushoUsafishajiBanda.objects.all()
    if users.exists():
        dynamic_interval = users[0].SikuZaKukumbushwa  # Kwa mfano, tumia thamani ya kwanza
        print(f"DYNAMIC {dynamic_interval}")
        # Panga kazi kwa kutumia dynamic interval
        schedule.every(dynamic_interval).seconds.do(job)
    else:
        print("Hakuna watumiaji waliopatikana.")

    while True:
        schedule.run_pending()
        tm.sleep(1)
