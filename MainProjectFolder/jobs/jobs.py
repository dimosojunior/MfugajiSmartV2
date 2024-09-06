from django.conf import settings
from django.core.mail import send_mail
from App.models import *

def schedule_api():
    # orders = HotelRoomsOrderItems.objects.filter(DaysNumber=1)

    # for order in orders:
    #     # Send an email to the user
    #     email = order.Customer.CustomerEmail
    #     subject = "Easy-Fix"
    #     message = "Muda 16 wako wa kuendelea kukaa chumbani umekwisha, jiandae kwa ajili ya kutoka"
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [email]
    #     send_mail(subject, message, from_email, recipient_list, fail_silently=True)

    #     # Change RoomStatus in HotelRooms model to False
    #     room = order.room
    #     room.RoomStatus = False
    #     room.ProductQuantity = 1
    #     room.save()

    #     print(f"Email: {recipient_list}")
    #     print("HELLO")


    # users = MyUser.objects.all()

    # for item in users:
    #     # Send an email to the user
    #     email = item.email
    #     subject = "Easy-Fix"
    #     message = "Email kutoka Mfugaji App"
    #     from_email = settings.EMAIL_HOST_USER
    #     recipient_list = [email]
    #     send_mail(subject, message, from_email, recipient_list, fail_silently=True)

        

    #     print(f"Email: {recipient_list}")

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


#schedule_api()
