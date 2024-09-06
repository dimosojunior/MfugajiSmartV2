from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events
from django.core.mail import send_mail
from django.conf import settings
from App.models import KumbushoLaChanjo
from django.db.models import F
import schedule
import time as tm

def weekly_vaccine_reminder():
    print("Scheduler job started")
    users = KumbushoLaChanjo.objects.all()

    for item in users:
        # Retrieve the current UmriWaKukuKwaSiku value
        current_umri = item.UmriWaKukuKwaSiku
        #print(f"current Umri: {current_umri}")

        if current_umri is None:
            current_umri = 0  # Handle initial value if None

        
        # Check if it's the first iteration (value from database), don't increment

        if current_umri != '0':
            # Increment UmriWaKukuKwaSiku by 7 for subsequent iterations
            item.UmriWaKukuKwaSiku = str(int(current_umri) + 7)
            item.save()

        UmriWaKukuKwaSiku = int(item.UmriWaKukuKwaSiku)

        AinaYaKuku = item.AinaYaKuku.AinaYaKuku
        username = item.username

        # Retrieve the first selected AinaYaChanjo item where UmriWaKukuKwaSiku >= Kutolewa
        #hapa tunataka kumtajia ni chanjo kwa muda huo anatakiwa kupata, kwanyio kama kuku wake
        #wana siku 7 maana yake tutampa chanjo zote ambazo siku ya kutolewa ni kubwa au sawa na
        #umri wa kuku wake ila zinaweza zikawa kubwa nyingi ila tunampa ile ya kwanza, lakini 
        #unapaswa kunoti kama kuku ana wiki 7 maana yake chanjo ya wiki hiyo ya saba hatutomkubusha
        #kwahiyo tutaanza kumkumbusha ya siku ya 14, kwahiyo kabla ya kukompare tunajumlisha umri
        #wa kuku wake + 7, then tunapata 14, halafu ndo tunaenda kuangalia je ni chanjo ya kwanza
        #siku ya kutolewa ni kubwa au sawa na 14, then tunamtajia hiyo chanjo

        #emailitaenda endapo hii condition ni true
        selected_chanjo = item.AinaYaChanjo.filter(
            Kutolewa=UmriWaKukuKwaSiku
        ).first()

        if selected_chanjo:
            chanjo_name = selected_chanjo.JinaLaChanjo

            # Send an email to the user
            email = item.email
            subject = "Mfugaji Smart"
            message = f"Hello {username}, leo ni siku ya kuku wako kupata chanjo, hivyo unakumbushwa kuwapa kuku wako aina ya {AinaYaKuku} wenye umri wa siku {UmriWaKukuKwaSiku} chanjo ya {chanjo_name}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            print(f"Jina: {username}, Chanjo Ya Siku Ya: {UmriWaKukuKwaSiku}, Chanjo: {chanjo_name}")
            print(f"ANAFUATA MWINGINE \n \n")
        
        else:
            chanjo_name = "Hakuna Chanjo inayofaa kwa siku hii"
            print(f"HAKUNA EMAIL INAYOTUMWA KWASABABU HAKUNA CHANJO YA SIKU {UmriWaKukuKwaSiku}")

        


def chanjo_scheduler():
    users = KumbushoLaChanjo.objects.all()

    schedule.every(7).days.do(weekly_vaccine_reminder)

    while True:
        schedule.run_pending()
        tm.sleep(1)