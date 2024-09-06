from apscheduler.schedulers.background import BackgroundScheduler
from django_apscheduler.jobstores import DjangoJobStore, register_events, register_job
from App.models import *
from django.core.mail import send_mail
from django.conf import settings
from datetime import timedelta

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), "default")

    @register_job(scheduler, "interval", days=7, replace_existing=True)
    def weekly_vaccine_reminder():
        users = KumbushoLaChanjo.objects.all()

        for item in users:
            # Increase UmriWaKukuKwaSiku by 7
            item.UmriWaKuku.UmriKwaSiku += 7
            item.UmriWaKuku.save()

            UmriWaKukuKwaSiku = item.UmriWaKuku.UmriKwaSiku
            AinaYaKuku = item.AinaYaKuku.AinaYaKuku
            username = item.username

            # Retrieve the first selected AinaYaChanjo item where UmriWaKukuKwaSiku >= Kutolewa
            selected_chanjo = item.AinaYaChanjo.filter(
                    Kutolewa__lte=UmriWaKukuKwaSiku
                ).first()

            if selected_chanjo:
                chanjo_name = selected_chanjo.JinaLaChanjo
            else:
                chanjo_name = "Hakuna Chanjo inayofaa kwa siku hii"

            # Send an email to the user
            email = item.email
            subject = "Mfugaji Smart"
            message = f"Email kutoka Mfugaji Smart App. \n Hello {username}, leo ni siku ya kuku wako kupata chanjo, hivyo unakumbushwa kuwapa kuku wako aina ya {AinaYaKuku} wenye umri wa siku {UmriWaKukuKwaSiku} chanjo ya {chanjo_name}"
            from_email = settings.EMAIL_HOST_USER
            recipient_list = [email]
            send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            print(f"JIna: {username}, AinaYaKuku:{AinaYaKuku}, Umri: {UmriWaKukuKwaSiku}, Chanjo: {chanjo_name}")
            print(f"ANAFUATA MWINGINE \n \n")

    register_events(scheduler)
    scheduler.start()

# Call start() in your Django app's startup code, e.g., in the ready() method of an AppConfig subclass.
