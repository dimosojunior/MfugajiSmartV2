from django.conf import settings
from django.core.mail import send_mail
from App.models import KumbushoLaChanjo

def schedule_api():
    users = KumbushoLaChanjo.objects.all()

    for item in users:
        UmriWaKukuKwaSiku = item.UmriWaKuku.UmriKwaSiku
        AinaYaKuku = item.AinaYaKuku.AinaYaKuku
        username = item.username

        # Retrieve selected AinaYaChanjo items
        selected_chanjo = item.AinaYaChanjo.all()
        chanjo_list = ', '.join([chanjo.JinaLaChanjo for chanjo in selected_chanjo])

        # Send an email to the user
        email = item.email
        subject = "Mfugaji Smart"
        message = f"Email kutoka Mfugaji Smart App. \n Hello {username}, leo ni siku ya kuku wako kupata chanjo, hivyo unakumbushwa kuwapa kuku wako aina ya {AinaYaKuku} wenye umri wa siku {UmriWaKukuKwaSiku} chanjo ya {chanjo_list}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        print(f"JIna: {username}, AinaYaKuku:{AinaYaKuku}, Umri: {UmriWaKukuKwaSiku} message: {message}")
        print(f"ANAFUATA MWINGINE \n \n")

# schedule_api()
