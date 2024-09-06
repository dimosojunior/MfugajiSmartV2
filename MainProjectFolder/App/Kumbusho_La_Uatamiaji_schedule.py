import schedule
import time as tm
from django.conf import settings
from django.core.mail import send_mail
from App.models import *

def job(item):
    

    #for item in users:
    KiasiChaMayai = item.KiasiChaMayai
    SikuYaNgapiTokaKuatamiwa = item.SikuYaNgapiTokaKuatamiwa
    username = item.username
    AinaYaNdege = item.AinaYaNdege
    SikuKamiliZaKuatamia = item.SikuKamiliZaKuatamia
    JinaLaUlipoYatoaMayai = item.JinaLaUlipoYatoaMayai
    Kifaa = item.Kifaa
    phone = item.phone
    email = item.email

    SikuZaZiada = 3
    SikuYaNgapiTokaKuatamiwa_Zaidi = SikuYaNgapiTokaKuatamiwa + SikuZaZiada

    print(f"Username: {username}, SikuYaNgapiTokaKuatamiwa {SikuYaNgapiTokaKuatamiwa}, SikuYaNgapiTokaKuatamiwa_Zaidi {SikuYaNgapiTokaKuatamiwa_Zaidi}")

    Remained_Value = SikuKamiliZaKuatamia - SikuYaNgapiTokaKuatamiwa_Zaidi
    print(f"Remained Value: {Remained_Value}")

    if Remained_Value :

        # # Tuma barua pepe kwa mtumiaji
        email = email
        subject = "Mfugaji Smart"
        message = f"Kumbusho La Uatamiaji Uatamiaji : Email kutoka Mfugaji Smart App. \n Hello {username}, leo ni siku {Remained_Value} tangu mara ya mwisho mayai yako yenye alama (Mteja) {JinaLaUlipoYatoaMayai} kuatamiwa siku {SikuYaNgapiTokaKuatamiwa}, hivyo bado siku {SikuZaZiada} mayai yako kuatamiwa.\n \n Aina ya ndege {AinaYaNdege} \n \n kifaa unachotumia {Kifaa}"
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email]
        send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    
    #print(f"Another One \n \n")

# Pata thamani ya dynamic variable
def Kumbusho_La_Uatamiaji_start_scheduler():
    users = KumbushoLaUatamiajiWaMayai.objects.all()
    for item in users:
        KiasiChaMayai = item.KiasiChaMayai
        SikuYaNgapiTokaKuatamiwa = item.SikuYaNgapiTokaKuatamiwa
        username = item.username
        AinaYaNdege = item.AinaYaNdege
        SikuKamiliZaKuatamia = item.SikuKamiliZaKuatamia
        JinaLaUlipoYatoaMayai = item.JinaLaUlipoYatoaMayai
        Kifaa = item.Kifaa
        phone = item.phone
        email = item.email

        SikuZaZiada = 3
        SikuYaNgapiTokaKuatamiwa_Zaidi = SikuYaNgapiTokaKuatamiwa + SikuZaZiada

        #print(f"Username: {username}, SikuYaNgapiTokaKuatamiwa {SikuYaNgapiTokaKuatamiwa}, SikuYaNgapiTokaKuatamiwa_Zaidi {SikuYaNgapiTokaKuatamiwa_Zaidi}")

        Remained_Value = SikuKamiliZaKuatamia - SikuYaNgapiTokaKuatamiwa_Zaidi
        #print(f"Remained Value: {Remained_Value}")


        if Remained_Value:  # Ensure SikuZaKukumbushwa is not None
            schedule.every(Remained_Value).seconds.do(job, item=item)

            # Tuma barua pepe kwa mtumiaji
            # email = email
            # subject = "Mfugaji Smart"
            # message = f"Kumbusho La Uatamiaji Uatamiaji : Email kutoka Mfugaji Smart App. \n Hello {username}, leo ni siku {Remained_Value} tangu mara ya mwisho mayai yako yenye alama (Mteja) {JinaLaUlipoYatoaMayai} kuatamiwa siku {SikuYaNgapiTokaKuatamiwa}, hivyo bado siku {SikuZaZiada} mayai yako kuatamiwa.\n \n Aina ya ndege {AinaYaNdege} \n \n kifaa unachotumia {Kifaa}"
            # from_email = settings.EMAIL_HOST_USER
            # recipient_list = [email]
            # send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        else:
            print("Hakuna watumiaji waliopatikana.")

    while True:
        schedule.run_pending()
        tm.sleep(1)
