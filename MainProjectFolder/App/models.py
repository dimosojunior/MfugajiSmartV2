from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
#from ckeditor_uploader.fields import RichTextUploadingField
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils import timezone
from django.conf import settings
from django.db.models.signals import pre_save,post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractBaseUser
import random
from datetime import timedelta
# Create your models here.



class AinaZaKuku(models.Model):
    
    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=100, blank=False,null=False)

    #hivi ni vipindi vya chakula vinavyoanza mpk vinapoishia
    #na vinachukua interval gani na kwa wiki ngapi kulingana
    #na aina ya kuku
    StaterFeed = models.CharField(verbose_name="Stater Feed",max_length=200, blank=True,null=True)
    GrowerFeed = models.CharField(verbose_name="Grower Feed",max_length=200, blank=True,null=True)
    FinisherFeed = models.CharField(verbose_name="Finisher Feed",max_length=200, blank=True,null=True)
    LayerFeed = models.CharField(verbose_name="Layer Feed",max_length=200, blank=True,null=True)

    #hizi ni total percentages required kwa kila aina ya
    #kipindi cha chakula ambazo hizi kule kwenye model
    #ya vyakula wkt wa kukokotoa baada ya kupata total
    #percentage ya kila kirutubisho tunakuja kukompare na
    #hii km ni ndogo tunampa ushauri,
    #ila hapa tunatumia makundi 3 tu ya virutubisho mengine
    #tunaachana nayo
    TotalCPPercentageRequired_Starter = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Starter - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Starter = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Starter - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Starter = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Starter - %", default=0, blank=True,null=True)

    TotalCPPercentageRequired_Grower = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Grower - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Grower = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Grower - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Grower = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Grower - %", default=0, blank=True,null=True)

    TotalCPPercentageRequired_Layer = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Layer - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Layer = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Layer - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Layer = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Layer - %", default=0, blank=True,null=True)

    TotalCPPercentageRequired_Finisher = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha CP Kwenye Kipindi  Cha Finisher - %", default=0, blank=True,null=True)
    TotalWangaPercentageRequired_Finisher = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Wanga Kwenye Kipindi  Cha Finisher - %", default=0, blank=True,null=True)
    TotalMafutaPercentageRequired_Finisher = models.IntegerField(verbose_name="Kiwango Cha Jumla Cha Mafuta Kwenye Kipindi  Cha Finisher - %", default=0, blank=True,null=True)

    PichaYaKuku = models.ImageField(verbose_name="Picha Ya Kuku", upload_to='media/PichaZaKuku/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaKuku}"
    
    class Meta:
        verbose_name_plural = "Aina Za Kuku"

class AinaZaNdege(models.Model):
    
    AinaYaNdege = models.CharField(verbose_name="Aina Ya Ndege",max_length=100, blank=False,null=False)
    SikuKamiliZaKuatamia = models.IntegerField(verbose_name="Siku Kamili Za Kuatamia", blank=True,null=True)
    StaterFeed = models.CharField(verbose_name="Stater Feed",max_length=200, blank=True,null=True)
    GrowerFeed = models.CharField(verbose_name="Grower Feed",max_length=200, blank=True,null=True)
    FinisherFeed = models.CharField(verbose_name="Finisher Feed",max_length=200, blank=True,null=True)
    LayerFeed = models.CharField(verbose_name="Layer Feed",max_length=200, blank=True,null=True)

    PichaYaNdege = models.ImageField(verbose_name="Picha Ya Ndege", upload_to='media/PichaZaKuku/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaNdege}"
    
    class Meta:
        verbose_name_plural = "Aina Za Ndege"


class Mikoa(models.Model):
    
    JinaLaMkoa = models.CharField(verbose_name="Jina La Mkoa",max_length=100, blank=False,null=False)
    Kanda = models.CharField(verbose_name="Kanda",max_length=500, blank=True,null=True) 
    #Chakula = models.ForeignKey('Vyakula', verbose_name="Aina Ya Chakula",on_delete=models.CASCADE, blank=True,null=True)
    #price = models.FloatField(verbose_name="Bei Ya Chakula", blank=True,null=True) 
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaMkoa}"
    
    class Meta:
        verbose_name_plural = "Mikoa"

class LevelZaWafugaji(models.Model):
    
    Level = models.CharField(verbose_name="Level Ya Mfugaji",max_length=100, blank=False,null=False)
    Nyota = models.CharField(verbose_name="Kanda",max_length=500, blank=True,null=True) 
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Level}"
    
    class Meta:
        verbose_name_plural = "LevelZaWafugaji"


class UserStatus(models.Model):
    
    Status = models.CharField(verbose_name="Status",max_length=100, blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Status}"
    
    class Meta:
        verbose_name_plural = "Status Za Wafugaji"

class UserRole(models.Model):
    
    Role = models.CharField(verbose_name="Aina Ya User",max_length=100, blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.Role}"
    
    class Meta:
        verbose_name_plural = "User Role"



# class SikuZaKusafishaBanda(models.Model):
    
#     Siku = models.IntegerField(verbose_name="Siku ?", blank=False,null=False)
#     Wiki = models.IntegerField(verbose_name="Wiki ? (Usijaze)", blank=True,null=True)
#     Mwezi = models.IntegerField(verbose_name="Mwezi ? (Usijaze)", blank=True,null=True)
#     Created = models.DateTimeField(auto_now_add=True)
#     Updated = models.DateTimeField(auto_now=True)
    
#     def __str__(self):
#         return f"Siku {self.Siku}, Wiki {self.Wiki}"
    
#     class Meta:
#         verbose_name_plural = "Siku Za Kusafisha Banda"





class MudaWaKumbushoUsafishajiBanda(models.Model):
    
    Muda = models.CharField(verbose_name="Jina La Muda",max_length=100, blank=False,null=False)
    StartingTime = models.TimeField(auto_now_add=False, verbose_name="Muda Wa Kuanza", blank=False,null=False)
    EndingTime = models.TimeField(auto_now_add=False, verbose_name="Muda Wa Kuisha", blank=False,null=False)
    
    def __str__(self):
        return f"{self.Muda} Kuanzia {self.StartingTime} Mpaka {self.EndingTime}"
    
    class Meta:
        verbose_name_plural = "Muda Wa Kumbusho Usafishaji Banda"



class KumbushoUsafishajiBanda(models.Model):
    SikuZaKukumbushwa = models.IntegerField(verbose_name="Ukumbushwe Baada Ya Siku ?", blank=True,null=True)   
    Muda = models.ForeignKey(MudaWaKumbushoUsafishajiBanda, verbose_name="Muda Wa Kukumbushwa", blank=True,null=True,on_delete=models.CASCADE)

    Awamu_Choices = (
            ('Ijirudie', 'Ijirudie'),
            ('Maramoja tu', 'Maramoja tu'),

        )
    Awamu = models.CharField(choices=Awamu_Choices, verbose_name="Awamu Za Ukumbushwaji",max_length=100, blank=True,null=True)

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)
    SikuZaKukumbushwaDisplayedValue = models.IntegerField(verbose_name="Ukumbushwe Baada Ya Siku (TunayotumiaKudisplay- Usijaze) ?", blank=True,null=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone} Siku {self.SikuZaKukumbushwa}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Usafishaji Banda"


#hizi ni calculation za kupatahizo field mbili za juu ambazo tutazitumia kwenye
#templates kumuindicate admin user yupi anapaswa kukumbushwa, kwa yule mwenye
#background nyekundi anapaswa kukumbushwa
    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        # print(f"Time Now: {timezone.now()}")
        # print(f"Time Since {time_elapsed} days")
        # print(f"Siku Za Kukumbushwa {self.SikuZaKukumbushwa} days")
        
        # Assuming SikuZaKukumbushwa is the number of days, directly subtract time_elapsed
        remaining_days = self.SikuZaKukumbushwa - time_elapsed
        #print(f"Time Left: {remaining_days} days")

        # Update day_is_reached to True if remaining_days is equal to 1
        if remaining_days == 1 and not self.day_is_reached:
            self.day_is_reached = True
            self.save(update_fields=['day_is_reached'])

        return remaining_days

    @property
    def is_red(self):
        #background iwe red endapo ukichukua siku alizotaka kukumbushwa - muda wa sasa
        #sawasawa na siku 1 background iwe nyekundu, maana yake tunamkumbusha user
        #siku moja kabla sa siku aliyoweka
        
        return self.time_left == 1













class MyUserManager(BaseUserManager):
    def create_user(self, email, username,phone, password=None):
        if not email:
            raise ValueError("email is required")
        if not username:
            raise ValueError("Your user name is required")


        
        

        user=self.model(
            email=self.normalize_email(email),
            username=username,
            phone=phone,
            
            
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, phone, username, password=None):
        user=self.create_user(
            email=self.normalize_email(email),
            username=username,
            password=password,
            phone=phone,

        )
        user.is_admin=True
        user.is_staff=True
        user.is_customer=False
        
        user.is_superuser=True
        user.save(using=self._db)
        return user

    

  
class MyUser(AbstractBaseUser):
    email=models.EmailField(verbose_name="email", max_length=100, unique=True)
    first_name=models.CharField(verbose_name="first name", max_length=100, unique=False)
    username=models.CharField(verbose_name="user name", max_length=100, unique=True)
    middle_name=models.CharField(verbose_name="middle name", max_length=100, unique=False)
    last_name=models.CharField(verbose_name="last name", max_length=100, unique=False)
    company_name=models.CharField(verbose_name="company name",blank=True,null=True, max_length=500, unique=False)
    phone=models.CharField(verbose_name="phone", max_length=13)
    Location=models.CharField(verbose_name="Mahali", max_length=200, blank=True, null=True)
    Mkoa = models.ForeignKey(Mikoa, verbose_name="Mkoa",on_delete=models.CASCADE, blank=True,null=True)
    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku",on_delete=models.CASCADE, blank=True,null=True)
    Role = models.ForeignKey(UserRole, verbose_name="Aina Ya User",on_delete=models.CASCADE, blank=True,null=True)
    #hizi mbili zinakuwa approved by admin
    Level = models.ForeignKey(LevelZaWafugaji, verbose_name="Level Ya Mfugaji",on_delete=models.CASCADE, blank=True,null=True)
    Tick_choises = (
        ('Ndio Anastahili', 'Ndio Anastahili'),
        ('Hapana Hastahili', 'Hapana Hastahili')

    )
    Tick = models.CharField(choices=Tick_choises,max_length=100, verbose_name="Anastahili Tiki ?", blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    OmbaNyota = models.TextField(max_length=10000, blank=True,null=True)
    PichaYaLeseni = models.ImageField(upload_to='media/',verbose_name="Picha Ya Leseni", blank=True, null=True)
    LevelImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Nyota", blank=True, null=True)
    #phone=models.CharField(verbose_name="phone", max_length=15)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Ya Mtu", blank=True, null=True)
    date_joined=models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    # Role_Choices = (
    #         ('MULTI TEACHER', 'MULTI TEACHER'),
    #         ('PHYSICS TEACHER', 'PHYSICS TEACHER'),
    #         ('CHEMISTRY TEACHER', 'CHEMISTRY TEACHER'),
    #         ('BIOLOGY TEACHER', 'BIOLOGY TEACHER'),
    #         ('ENGLISH TEACHER', 'ENGLISH TEACHER'),
    #         ('CIVICS TEACHER', 'CIVICS TEACHER'),
    #         ('MATHEMATICS TEACHER', 'MATHEMATICS TEACHER'),
    #         ('HISTORY TEACHER', 'HISTORY TEACHER'),
    #         ('GEOGRAPHY TEACHER', 'GEOGRAPHY TEACHER'),
    #         ('KISWAHILI TEACHER', 'KISWAHILI TEACHER'),
    #     )

    # role=models.CharField(verbose_name="role", choices=Role_Choices, max_length=50)
    last_login=models.DateTimeField(verbose_name="last login", auto_now=True)
    is_admin=models.BooleanField(default=False)
    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=True)
    is_superuser=models.BooleanField(default=False)
    is_customer=models.BooleanField(default=True)

    hide_email = models.BooleanField(default=True)

    


    USERNAME_FIELD="username"
    REQUIRED_FIELDS=['email','phone']
    
    objects=MyUserManager()

    def __str__(self):
        return self.username


    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True






class OTP(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    otp = models.CharField(max_length=6)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        if not self.otp:
            self.otp = ''.join([str(random.randint(0, 9)) for _ in range(6)])
        super().save(*args, **kwargs)

    def is_valid(self):
        from django.utils import timezone
        return self.created_at >= timezone.now() - timezone.timedelta(minutes=10)













class Notification(models.Model):
    #user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='notifications')
    PostOwner = models.CharField(verbose_name="Mmiliki Wa Posti: ", max_length=200, blank=True,null=True)
    username = models.CharField(verbose_name="Aliye Like Ni: ", max_length=200, blank=True,null=True)
    duka_lako = models.CharField(verbose_name="Post Aliyo Like: ", max_length=1000, blank=True,null=True)
    message = models.TextField()
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    #hii ni picha ya mtu aliyelike
    Photo = models.ImageField(upload_to='media/',verbose_name="Picha Ya Aliye Like", blank=True, null=True)

    Maelezo = models.TextField(max_length=10000, blank=True,null=True)
    PichaYaPost = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post", blank=True, null=True)
    PichaYaPost2 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 2", blank=True, null=True)
    PichaYaPost3 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 3", blank=True, null=True)
    PichaYaPost4 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 4", blank=True, null=True)
    PichaYaPost5 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 5", blank=True, null=True)
    
    #-------hizi ni taarifa za aliyelike
    phone = models.CharField(verbose_name="Namba Yake ya Simu",max_length=13, blank=True,null=True)  
    email = models.EmailField(verbose_name="Email Yake",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali Anapoishi",max_length=200, blank=True,null=True)
    #Likes = models.IntegerField(verbose_name="Post Likes",default=0, blank=True,null=True)
    #liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_dukalako', blank=True)


    def __str__(self):
        return f"Notification for {self.username} - {self.duka_lako}"




class DukaLako(models.Model):
    Title = models.CharField(verbose_name="Kinahusiana Na ?", max_length=500, blank=True,null=True)
    Maelezo = models.TextField(max_length=10000, blank=False,null=False)
    PichaYaPost = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post", blank=True, null=True)
    PichaYaPost2 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 2", blank=True, null=True)
    PichaYaPost3 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 3", blank=True, null=True)
    PichaYaPost4 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 4", blank=True, null=True)
    PichaYaPost5 = models.ImageField(upload_to='media/',verbose_name="Picha Ya Post 5", blank=True, null=True)

    Status = models.ForeignKey(UserStatus, verbose_name="Status",on_delete=models.CASCADE, blank=True,null=True)
    
    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    UserRole = models.CharField(verbose_name="Aina Ya Mtumiaji",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Yako", blank=True, null=True)
    LevelImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Nyota", blank=True, null=True)
    Likes = models.IntegerField(verbose_name="Post Likes",default=0, blank=True,null=True)
    liked_by = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='liked_dukalako', blank=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone} - {self.Title}"
    
    class Meta:
        verbose_name_plural = "Duka Lako"








class Maoni(models.Model):
    Maoni = models.TextField(max_length=10000, blank=False,null=False)
    
    
    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=13, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)
    profile_image = models.ImageField(upload_to='media/',verbose_name="Picha Yako", blank=True, null=True)
    LevelImage = models.ImageField(upload_to='media/',verbose_name="Picha Ya Nyota", blank=True, null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone} - {self.Maoni}"
    
    class Meta:
        verbose_name_plural = "Maoni"












class Huduma(models.Model):
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=100, blank=False,null=False)
    PichaYaHuduma = models.ImageField(verbose_name="Picha Ya Huduma", upload_to='media/PichaZaHuduma/',blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaHuduma}"
    
    class Meta:
        verbose_name_plural = "Huduma"

class MgawanjoWaHuduma(models.Model):
    Category = models.ForeignKey(Huduma, verbose_name="Category",on_delete=models.CASCADE, blank=True,null=True)
    
    JinaLaHuduma = models.CharField(verbose_name="Jina La Huduma",max_length=100, blank=False,null=False)
    PichaYaHuduma = models.ImageField(verbose_name="Picha Ya Huduma", upload_to='media/PichaZaHuduma/',blank=True,null=True)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaHuduma}"
    
    class Meta:
        verbose_name_plural = "Mgawanjo Wa Huduma"



class IdadiYaKuku(models.Model):
    
    IdadiYaKuku = models.IntegerField(verbose_name="Idadi Ya Kuku", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Kuku {self.IdadiYaKuku}"
    
    class Meta:
        verbose_name_plural = "Idadi Ya Kuku"


class IdadiYaKilos(models.Model):
    
    IdadiYaKilos = models.IntegerField(verbose_name="Idadi Ya Kilos", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Kilos {self.IdadiYaKilos}"
    
    class Meta:
        verbose_name_plural = "Idadi Ya Kilos"


class UmriWaKuku(models.Model):
    
    UmriKwaWiki = models.IntegerField(verbose_name="Wiki ?", blank=False,null=False)
    UmriKwaSiku = models.IntegerField(verbose_name="Siku ? (Usijaze)", blank=True,null=True)
    Interval = models.CharField(verbose_name="Interval",max_length=100, blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.UmriKwaWiki}, Siku {self.Interval}"
    
    class Meta:
        verbose_name_plural = "Umri Wa Kuku"



@receiver(pre_save, sender=UmriWaKuku)
def set_UmriKwaSiku(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.UmriKwaSiku = instance.UmriKwaWiki * 7



class Siku(models.Model):
    
    Siku = models.IntegerField(verbose_name="Siku ?", blank=False,null=False)
    Wiki = models.IntegerField(verbose_name="Wiki ? (Usijaze)", blank=True,null=True)
    Mwezi = models.IntegerField(verbose_name="Mwezi ? (Usijaze)", blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Siku {self.Siku} - Wiki {self.Wiki}  - Mwezi {self.Mwezi}"
    
    class Meta:
        verbose_name_plural = "Siku"


@receiver(pre_save, sender=Siku)
def set_Wiki(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        if instance.Siku < 7:
            instance.Wiki = 0
        instance.Wiki = int(instance.Siku / 7)

@receiver(pre_save, sender=Siku)
def set_Mwezi(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        if instance.Siku < 28:
            instance.Mwezi = 0
        instance.Mwezi = int(instance.Wiki / 4)







class MaktabaYaLisheCategories(models.Model):

    CategoryName = models.CharField(max_length=500,verbose_name="Category", blank=False,null=False)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Makundi Ya Maktaba Ya Lishe"

    def __str__(self):
        return self.CategoryName


class MaktabaYaLisheContents(models.Model):

    Title = models.CharField(max_length=5000,verbose_name="Title", blank=False,null=False)
    CategoryName = models.ForeignKey(MaktabaYaLisheCategories, verbose_name="Category",on_delete=models.CASCADE, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Ndani Ya Makundi Maktaba Ya Lishe"

    def __str__(self):
        return self.Title



class MuongozoWaLishe(models.Model):

    Title = models.CharField(max_length=5000,verbose_name="Title", blank=False,null=False)
    #CategoryName = models.ForeignKey(MaktabaYaLisheCategories, verbose_name="Category",on_delete=models.CASCADE, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Muongozo Wa Lishe"

    def __str__(self):
        return self.Title


class MatumiziSahihiYaIndibata(models.Model):

    Title = models.CharField(max_length=5000,verbose_name="Title", blank=False,null=False)
    #CategoryName = models.ForeignKey(MaktabaYaLisheCategories, verbose_name="Category",on_delete=models.CASCADE, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    YoutubeLinkVideo = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Matumizi Sahihi Ya Indibata"

    def __str__(self):
        return self.Title





class JamiiYaMfugajiCategories(models.Model):

    CategoryName = models.CharField(max_length=500,verbose_name="Category", blank=False,null=False)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name_plural = "Makundi Ya Jamii Ya Mfugaji"

    def __str__(self):
        return self.CategoryName






class JamiiYaMfugajiContents(models.Model):

    FullName = models.CharField(max_length=100,verbose_name="Jina Kamili", blank=False,null=False)
    Location = models.CharField(max_length=100,verbose_name="Mahali", blank=True,null=True)
    Title = models.CharField(max_length=5000,verbose_name="Title", blank=True,null=True)
    CategoryName = models.ForeignKey(JamiiYaMfugajiCategories, verbose_name="Category",on_delete=models.CASCADE, blank=True,null=True)
    Picha = models.ImageField(verbose_name="Picha", upload_to='media/PichaZaVirutubisho/',blank=True,null=True)
    Description = models.TextField(max_length=10000, blank=True,null=True)
    pdf = models.FileField(upload_to="media/MaktabaYaLishePDF",blank=True,null=True)
    #Prepared_By = models.CharField(max_length=500,verbose_name="Imeandaliwa Na:", blank=True,null=True)
    Email = models.EmailField(max_length=100,blank=True,null=True)
    Phone = models.CharField(default="+255", max_length=13,blank=True,null=True)
    #Github = models.CharField(default="https://github.com/dimosojunior/", max_length=1000,blank=True,null=True)
    Youtube = models.CharField(max_length=1000,blank=True,null=True)
    WhatsappLink = models.CharField(max_length=1000,blank=True,null=True)
    FaceBook = models.CharField(max_length=1000,blank=True,null=True)
    Instagram = models.CharField(max_length=1000,blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Ndani Ya Jamii Ya Mfugaji"

    def __str__(self):
        return self.FullName + " " + self.Title






class UnitZaVyakula(models.Model):
    
    Unit = models.CharField(verbose_name="Unit", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Unit
    
    class Meta:
        verbose_name_plural = "Unit Za Vyakula"


class MakundiYaVyakula(models.Model):
    
    Jina = models.CharField(verbose_name="Jina", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Jina
    
    class Meta:
        verbose_name_plural = "Makundi Ya Vyakula"

class VipindiVyaKuku(models.Model):
    
    Kipindi = models.CharField(verbose_name="Kipindi", max_length=500,blank=False,null=False)
    Muda = models.CharField(verbose_name="Muda",default="0-2", max_length=500,blank=False,null=False)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.Jina
    
    class Meta:
        verbose_name_plural = "Makundi Ya Vyakula"

class Vyakula(models.Model):
    
    
    product_name = models.CharField(verbose_name="Jina La Chakula", max_length=100,blank=False,null=False)
    FoodGroup = models.ForeignKey(MakundiYaVyakula, verbose_name="Kundi La Chakula",on_delete=models.CASCADE, blank=True,null=True)
    ProductDescription = models.TextField(verbose_name="Maelezo", max_length=10000,blank=True,null=True)
    InitialPrice = models.IntegerField(verbose_name="Bei Ya Mwanzo Ya Chakula", blank=True,null=True)
    price = models.FloatField(verbose_name="Bei Ya sasa Ya Chakula (Usijaze)", blank=True,null=True)   
    #ProductUnit = models.CharField(verbose_name="Product Unit", max_length=100,blank=True,null=True)
    ProductQuantity = models.FloatField(verbose_name="Kiasi - KG (Usijaze)",default=1, blank=True,null=True)
    #InitialProductQuantity = models.FloatField(verbose_name="Kiasi Cha Mwanzo Store-KG (Usijaze)",blank=True,null=True)    
    Unit = models.ForeignKey(UnitZaVyakula, verbose_name="Unit Ya Chakula",on_delete=models.CASCADE, blank=True,null=True)
    ProductImage = models.ImageField(verbose_name="Picha Ya Chakula", upload_to='media/PichaZaVyakula/',blank=True,null=True)

    

    #----------------MWANZO WA VIRUTUBISHO---------------------
    ME = models.FloatField(verbose_name="Kiwango Cha ME - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    CP = models.FloatField(verbose_name="Kiwango Cha CP - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Wanga = models.FloatField(verbose_name="Kiwango Cha Wanga - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Mafuta = models.FloatField(verbose_name="Kiwango Cha Mafuta - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    DCP = models.FloatField(verbose_name="Kiwango Cha DCP - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    PREMIX = models.FloatField(verbose_name="Kiwango Cha PREMIX - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Lysin  = models.FloatField(verbose_name="Kiwango Cha Lysin  - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    METH = models.FloatField(verbose_name="Kiwango Cha METH - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Tryptophan = models.FloatField(verbose_name="Kiwango Cha Tryptophan - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    UngaWaMifupa = models.FloatField(verbose_name="Kiwango Cha UngaWaMifupa - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)
    Chumvi = models.FloatField(verbose_name="Kiwango Cha Chumvi - % Kwenye 1Kg Ya Chakula", default=0, blank=True,null=True)


    #----------------PERCENTAGE YA KILA CHAKULA KWENYE MCHANGANYIKO---
    #hizi ni percentage ya kila chakula kinavyohitajika kwenye
    #mchanganyiko fulani wa chakula ambazo ni constant ila
    #zinabadilika kutokana na aina ya vipindi vya chakula
    #mfano percentage ya mahindi inayohitajika kwenye mchanganyiko
    #wa chakula kipindi cha starter ni tofauti na ile ya kipindi
    #cha grower kwahiyo zimekuwa categorized kwa magroup
    TotalPercentageRequired_Starter = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Starter - %", default=0, blank=True,null=True)
    TotalPercentageRequired_Grower = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Grower - %", default=0, blank=True,null=True)
    TotalPercentageRequired_Layer = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Layer - %", default=0, blank=True,null=True)
    TotalPercentageRequired_Finisher = models.FloatField(verbose_name="Kiwango Cha Chakula Kwenye Mchanganyiko Wa Jumla Wa Chakula Cha Finisher - %", default=0, blank=True,null=True)
    
    

    #Hutakiwi kujaza Hizi
    # Protini_In_1Kg = models.FloatField(verbose_name="Kiwango Cha Protini - % Kwenye 1Kg Ya Chakula", blank=True,null=True)

    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    
    
    class Meta:
        verbose_name_plural = "Vyakula"
        
    
    def __str__(self):
        return f" {self.product_name} "


# @receiver(pre_save, sender=ProductsStores)
# def Products__initial_quantity(sender, **kwargs):
#     Initial_qty = kwargs['instance']
#     Initial_qty.InitialProductQuantity = Initial_qty.ProductQuantity
#     # total_cart_items = CartItems.objects.filter(user = cart_items.user )
#     # cart = Cart.objects.get(id = cart_items.cart.id)
#     # cart.total_price = cart_items.price
#     # cart.save()

#@receiver(pre_save, sender=Vyakula)
# def set_initial_quantity(sender, instance, **kwargs):
#     # Check if the instance is new (i.e., it doesn't have a primary key yet)
#     if instance._state.adding:
#         instance.InitialProductQuantity = instance.ProductQuantity

@receiver(pre_save, sender=Vyakula)
def set_price_from_initial_price(sender, instance, **kwargs):
    # Check if the instance is new (i.e., it doesn't have a primary key yet)
    if instance._state.adding:
        instance.price = instance.InitialPrice








class VyakulaCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    total_price = models.FloatField(verbose_name="Jumla Ya Bei", default=0)
    total_Kilos = models.FloatField(verbose_name="Jumla Ya Kilos", default=0)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vyakula  Cart"

    def __str__(self):
        return str(self.user.username) + " " + str(self.total_price)
         


class VyakulaCartItems(models.Model):
    cart = models.ForeignKey(VyakulaCart, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Vyakula,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    #Customer = models.ForeignKey(ProductsCustomers,on_delete=models.CASCADE,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    #table = models.ForeignKey(ProductsTables,on_delete=models.CASCADE,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vyakula  Cart Items"
    
    def __str__(self):
        return f" {self.product.product_name}"
        
    

@receiver(pre_save, sender=VyakulaCartItems)
def Vyakula__correct_price(sender, **kwargs):
    cart_items = kwargs['instance']
    price_of_product = Vyakula.objects.get(id=cart_items.product.id)
    cart_items.price = cart_items.quantity * float(price_of_product.price)
    # total_cart_items = CartItems.objects.filter(user = cart_items.user )
    # cart = Cart.objects.get(id = cart_items.cart.id)
    # cart.total_price = cart_items.price
    # cart.save()







class VyakulaOrder(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,blank=True, null=True)
    cart = models.ForeignKey(VyakulaCart, on_delete=models.CASCADE, blank=True, null=True)
    # orderItems = models.ManyToManyField('ProductsOrderItems')
    total_price = models.FloatField(verbose_name="Jumla Ya Bei")
    total_Kilos = models.FloatField(verbose_name="Jumla Ya Kilos")

    TotalFoodMixerPercentage = models.FloatField(verbose_name="Jumla Ya Percentage Ya Vyakula Vyote (Variables Food) - %", default=0, null=True, blank=True)
    
    TotalConstantFoodMixerPercentage = models.FloatField(verbose_name="Jumla Ya Percentage Ya Vyakula Vyote (constant Food) - %", default=0, null=True, blank=True)
    TotalMixerKios_ForConstantFoodGroups = models.FloatField(verbose_name="Jumla Ya Kiasi Ya Vyakula Vyote Vilivyochagualiwa kutoka kwenye (constant Food Groups) - Kg", default=0, null=True, blank=True)

    #-----------ZOTE ZINAJIADD AUTOMATIC-----------------
    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=200, blank=True,null=True)
    StaterFeed = models.CharField(verbose_name="Stater Feed",max_length=200, blank=True,null=True)
    GrowerFeed = models.CharField(verbose_name="Grower Feed",max_length=200, blank=True,null=True)
    FinisherFeed = models.CharField(verbose_name="Finisher Feed",max_length=200, blank=True,null=True)
    LayerFeed = models.CharField(verbose_name="Layer Feed",max_length=200, blank=True,null=True)
    UmriKwaSiku = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Siku", default=0, null=True, blank=True)

    TotalFoodAmount = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha Chakula - Kg", default=0, null=True, blank=True)
    TotalCPPercentageRequired = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha CP Kwenye Chakula - %", default=0, null=True, blank=True)
    TotalWangaPercentageRequired = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha Wanga Kwenye Chakula - %", default=0, null=True, blank=True)
    TotalMafutaPercentageRequired = models.FloatField(verbose_name="Jumla Ya  Kiasi Cha Mafuta Kwenye Chakula - %", default=0, null=True, blank=True)

    #CategoryId = models.IntegerField(verbose_name="Category ID",blank=True,null=True)
    #closed_order_state = models.BooleanField(verbose_name="Is Order Closed ?", default=False,blank=True,null=True)
    Customer = models.CharField(max_length=500, verbose_name="Imewekwa Na:",blank=True,null=True)

    # table_number = models.CharField(max_length=500, verbose_name="Table Number",blank=True,null=True)

    #order_status = models.BooleanField(verbose_name="Status", default=False,blank=True,null=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Vyakula Orders"

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"


class VyakulaOrderItems(models.Model):
    order = models.ForeignKey(VyakulaOrder, on_delete=models.CASCADE) 
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Vyakula,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    # Customer = models.ForeignKey(ProductsCustomers,on_delete=models.CASCADE,blank=True,null=True)
    #order_status = models.BooleanField(verbose_name="Status", default=False,blank=True,null=True)
    quantity = models.IntegerField(default=1)
    # table = models.ForeignKey(ProductsTables,on_delete=models.CASCADE,blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = "Vyakula Orders Items"

    def __str__(self):
        return f" {self.product.product_name}" 








class Virutubisho(models.Model):
    JinaLaChakula = models.ForeignKey(Vyakula, verbose_name="Jina La Chakula",on_delete=models.CASCADE, blank=True,null=True)  
    Protini = models.IntegerField(verbose_name="Kiwango Cha Protini- %", blank=False,null=False)
    Cabohydrate = models.IntegerField(verbose_name="Kiwango Cha Cabohydrate- %", blank=False,null=False)
    Wanga = models.IntegerField(verbose_name="Kiwango Cha Wanga- %", blank=False,null=False)
    Fati = models.IntegerField(verbose_name="Kiwango Cha Fati- %", blank=False,null=False)
    Vitamini = models.IntegerField(verbose_name="Kiwango Cha Vitamini- %", blank=False,null=False)
    
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Wiki {self.JinaLaChakula.product_name}"
    
    class Meta:
        verbose_name_plural = "Umri Wa Kuku"












class AinaZaChanjo(models.Model):
    
    JinaLaChanjo = models.CharField(verbose_name="Jina La Chanjo",max_length=200, blank=False,null=False)
    Kutolewa = models.IntegerField(verbose_name="Hutolewa Siku Ya Ngapi ?",blank=True,null=True)
    MaelezoYaChanjo = models.TextField(verbose_name="Maelezo Ya Chanjo",max_length=10000, blank=True,null=True)
    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.JinaLaChanjo} Siku Ya {self.Kutolewa}"
    
    class Meta:
        verbose_name_plural = "Aina Za Chanjo"











class KumbushoLaMabadilikoYaLishe(models.Model):
      
    
    #--------HIZI ZINZJIJAZA ZENYEWE KWENYE VIEW------------------
    Lengo_Choices = (
            ('Nafuga kwa ajili ya mayai', 'Nafuga kwa ajili ya mayai'),
            ('Nafuga kwa ajili ya nyama', 'Nafuga kwa ajili ya nyama'),

        )
    LengoLaKufuga = models.CharField(choices=Lengo_Choices, verbose_name="Lengo La Kufuga Hao Kuku ?",max_length=500, blank=True,null=True)
    KundiLaKukuWake = models.CharField(verbose_name="Kundi La Kuku Wake",max_length=500, blank=True,null=True)

    AinaYaKuku = models.CharField(verbose_name="Aina Ya Kuku",max_length=500, blank=True,null=True)
    UmriWaKukuKwaSiku = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Siku", blank=True,null=True)
    UmriWaKukuKwaWiki = models.IntegerField(verbose_name="Umri Wa Kuku Kwa Wiki", blank=True,null=True)

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.username} Lengo: {self.LengoLaKufuga}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Mabadiliko Ya Lishe"




class KumbushoLaChanjo(models.Model):
      
    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku", blank=True,null=True,on_delete=models.CASCADE)
    #UmriWaKuku = models.ForeignKey(UmriWaKuku, verbose_name="Umri Wa Kuku", blank=False,null=False,on_delete=models.CASCADE)
    AinaYaChanjo = models.ManyToManyField(AinaZaChanjo, verbose_name="Aina Ya Chanjo", blank=True)

    #--------HIZI ZINZJIJAZA ZENYEWE KWENYE VIEW------------------
    UmriWaKukuKwaSiku = models.CharField(verbose_name="Umri Wa Kuku Kwa Siku",max_length=500, blank=True,null=True)
    UmriWaKukuKwaWiki = models.CharField(verbose_name="Umri Wa Kuku Kwa Wiki",max_length=500, blank=True,null=True)

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)
    
    
    def __str__(self):
        return f"{self.username} Simu {self.phone}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Chanjo"


    
    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days

        selected_chanjo = self.AinaYaChanjo.all()

        if selected_chanjo:
            for item in selected_chanjo:
                chanjo_name = item.JinaLaChanjo
                Hutolewa_Siku = item.Kutolewa
                remaining_days = Hutolewa_Siku - time_elapsed
                print(f"{self.username}, chanjo_name: {chanjo_name}, Hutolewa_Siku: {Hutolewa_Siku}, remaining_days: {remaining_days}")

                # Check if remaining days is 1 and set day_is_reached if not already set
                if remaining_days == 1 and not self.day_is_reached:
                    self.day_is_reached = True
                    self.save(update_fields=['day_is_reached'])

                # Return the remaining days for the first match (for display)
                return remaining_days

        # If no matching chanjo
        return None

    @property
    def is_red(self):
        # Will return True if any of the selected chanjo's remaining days is 1
        return self.time_left == 1







class KumbushoLaUatamiajiWaMayai(models.Model):
    KiasiChaMayai = models.IntegerField(verbose_name="Kiasi Cha Mayai", blank=False,null=False)
    SikuYaNgapiTokaKuatamiwa = models.IntegerField(verbose_name="Siku Ya Ngapi Tangu Kuatamiwa", blank=False,null=False)
    AinaYaNdege = models.CharField(verbose_name="Aina Ya Ndege",max_length=200, blank=True,null=True)
    SikuKamiliZaKuatamia = models.IntegerField(verbose_name="Siku Zake kamili za Ndege Kuatamia", blank=True,null=True)

    #AinaYaNdege = models.ForeignKey(AinaZaNdege, verbose_name="Aina Ya Ndege", blank=True,null=True,on_delete=models.CASCADE)
    JinaLaUlipoYatoaMayai = models.CharField(verbose_name="Jina La UlipoYatoa Mayai au Alama",max_length=200, blank=True,null=True)
    NambaYakeYaSimu = models.CharField(verbose_name="Namba yake Ya Simu",max_length=13, blank=True,null=True)
    Kifaa_Choices = (
            ('Incubator', 'Incubator'),
            ('Ndege Mwenyewe', 'Ndege Mwenyewe'),

        )
    Kifaa = models.CharField(choices=Kifaa_Choices, verbose_name="Unatumia nini Kuatamia ?",max_length=100, blank=True,null=True)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)

    time_left = models.IntegerField(blank=True, null=True)
    is_red = models.BooleanField(default=False)
    day_is_reached = models.BooleanField(default=False)
    message_is_sent = models.BooleanField(default=False)
    SikuKamiliZaKuatamiaDisplayed = models.IntegerField(verbose_name="Siku Zake kamili za Ndege Kuatamia (TunayotumiaKudisplay -Usijaze)", blank=True,null=True)
        
    
    def __str__(self):
        return f"{self.username} Simu {self.phone}"
    
    class Meta:
        verbose_name_plural = "Kumbusho La Uatamiaji Wa Mayai"




    @property
    def time_left(self):
        # Example calculation for time left
        time_elapsed = (timezone.now() - self.Created).days
        print(f"Time Since: {time_elapsed}")
        # print(f"Time Since {time_elapsed} days")
        # print(f"Siku Za Kukumbushwa {self.SikuZaKukumbushwa} days")
        kumbusho_la_mwisho = self.SikuYaNgapiTokaKuatamiwa
        siku_kamili_za_kuatamia_ndege = self.SikuKamiliZaKuatamia
        differ_days = siku_kamili_za_kuatamia_ndege - kumbusho_la_mwisho
        
        # Assuming SikuZaKukumbushwa is the number of days, directly subtract time_elapsed
        remaining_days = differ_days - time_elapsed
        print(f"Siku Ya Mwisho: {kumbusho_la_mwisho}, Siku Kamili: {siku_kamili_za_kuatamia_ndege}, Differ: {differ_days}, Time Left: {remaining_days} days")

        # Update day_is_reached to True if remaining_days is equal to 1
        if remaining_days == 2 and not self.day_is_reached:
            self.day_is_reached = True
            self.save(update_fields=['day_is_reached'])

        return remaining_days

    @property
    def is_red(self):
        #background iwe red endapo ukichukua siku alizotaka kukumbushwa - muda wa sasa
        #sawasawa na siku 1 background iwe nyekundu, maana yake tunamkumbusha user
        #siku moja kabla sa siku aliyoweka
        
        return self.time_left == 2
















class EmailSendCount_KumbushoLaUatamiajiWaMayai(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho La Uatamiaji Wa Mayai"





class EmailSendCount_KumbushoUsafishajiBanda(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    
    count = models.IntegerField(default=0)
    

    phone = models.CharField(verbose_name="Namba Yako ya Simu",max_length=13, blank=True,null=True)
    username = models.CharField(verbose_name="Jina Lako Kamili",max_length=500, blank=True,null=True)
    email = models.EmailField(verbose_name="Email Yako",max_length=200, blank=True,null=True)
    Location = models.CharField(verbose_name="Mahali",max_length=200, blank=True,null=True)
    #company_name = models.CharField(verbose_name="Kampuni/Jina La Biashara Yako",max_length=500, blank=True,null=True)


    last_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.count} times"

    class Meta:
        verbose_name_plural = "Email Count Kumbusho La Usafishaji Banda"




class TaarifaZaKuku(models.Model):

    # Hapa utajaza kila aina ya kuku na kwa kila Chakula na kwa kila wiki
    # Eg: AinaYaKuku: Stata
    #     UmriKwaWiki: Wiki 1
    #     JinaLaChakula: Mahindi
    #     KiwangoChaProtini_In_1Kg: 80%
    #     KiwangoChaWanga_In_1Kg: 80%, etc


    AinaYaKuku = models.ForeignKey(AinaZaKuku, verbose_name="Aina Ya Kuku",on_delete=models.CASCADE, blank=True,null=True)
    #UmriKwaWiki = models.ForeignKey(UmriWaKuku, verbose_name="Umri Wa Kuku - Wiki ?",on_delete=models.CASCADE, blank=True,null=True)
    #Kipindi = models.ForeignKey(VipindiVyaKuku, verbose_name="Kipindi",on_delete=models.CASCADE, blank=True,null=True)
    #JinaLaChakula = models.ForeignKey(Vyakula, verbose_name="Jina La Chakula",on_delete=models.CASCADE, blank=True,null=True)


    #--kiasi cha chakula KWA WIKI kulingana na umri wa kuku-----------------
    KiasiChaChakulaKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 1 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 2 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 3 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 4 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 5 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 6 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 7 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 8 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 9 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 10 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 11 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 12 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 13 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 14 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 15 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 16 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 17 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 18 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 19 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 20 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 21 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 22 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 23 - KG", default=0, blank=True,null=True)
    KiasiChaChakulaKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Wiki Kwa Kuku wa Wiki 24 - KG", default=0, blank=True,null=True)






    #------------------------ME------------------------------------
    # KiasiChaMEKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 1 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 2 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 3 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 4 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 5 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 6 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 7 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 8 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 9 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 10 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 11 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 12 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 13 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 14 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 15 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 16 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 17 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 18 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 19 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 20 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 21 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 22 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 23 - Kcal/kg", default=0, blank=True,null=True)
    # KiasiChaMEKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kwa Wiki Kwa Kuku wa Wiki 24 - Kcal/kg", default=0, blank=True,null=True)






    # #-------------------CP-----------------------------------------
    # KiasiChaCPKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaCPKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha CP Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)

    



    # #------------------------WANGA----------------------------
    # KiasiChaWangaKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaWangaKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Wanga Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)





    # #------------------------MAFUTA--------------------------
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaMafutaKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Mafuta Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)





    # #--------------------LYSIN--------------------------------
    # KiasiChaLysinKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaLysinKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Lysin Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)




    # #----------------------------METH-------------------
    # KiasiChaMETHKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaMETHKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha METH Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)







    # #--------------------------TRYPTO-----------------
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaTryptophanKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Tryptophan Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)





    # #-------------------DCP-----------------------
    # KiasiChaDCPKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaDCPKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha DCP Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)







    # #---------------------PREMIX------------------
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaPREMIXKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha PREMIX Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)





    # #-------------------------Unga Wa Mifupa-------------
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaUngaWaMifupaKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha UngaWaMifupa Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)





    # #----------------------CHUMVI---------------------
    # KiasiChaChumviKwaKukuWaUmriWaWiki_1_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 1 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_2_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 2 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_3_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 3 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_4_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 4 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_5_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 5 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_6_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 6 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_7_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 7 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_8_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 8 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_9_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 9 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_10_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 10 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_11_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 11 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_12_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 12 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_13_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 13 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_14_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 14 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_15_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 15 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_16_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 16 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_17_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 17 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_18_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 18 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_19_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 19 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_20_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 20 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_21_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 21 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_22_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 22 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_23_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 23 - %", default=0, blank=True,null=True)
    # KiasiChaChumviKwaKukuWaUmriWaWiki_24_KwaWiki = models.FloatField(verbose_name="Kiasi Cha Chumvi Kwa Wiki Kwa Kuku wa Wiki 24 - %", default=0, blank=True,null=True)





    #--------------MWISHO HAPA--------------------


    #KiasiChaChakulaKwaSiku = models.FloatField(verbose_name="Kiasi Cha Chakula Kwa Siku Kwa Kuku 1 - KG (Usijaze)", default=0, blank=True,null=True)

    
    

    
    #HIZI UNATAKIWA KUJAZA KWA WIKI
    #KiasiChaMEKilichopokwenye_KiasiChaChakulaKwaWiki = models.FloatField(verbose_name="Kiasi Cha ME Kinachohitajika Kwa Wiki Kwa Kuku 1 - Kca/Kg",default=0,  blank=True,null=True)
    

    

    

    Created = models.DateTimeField(auto_now_add=True)
    Updated = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.AinaYaKuku.AinaYaKuku}"
    
    class Meta:
        verbose_name_plural = "Taarifa Za Kuku"



#tunatumia hii ili baadhi ya field tuziadd automatically
#ili ukituma hii hta ukiupdate hata ile field ya automatically inajiupdate
# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_kiasi_cha_chakula_kwa_siku(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaChakulaKwaSiku = (quryset.KiasiChaChakulaKwaWiki) / 7
    

# #-----------------KWA ajili ya Virutubisho--------
# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaMEKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaMETHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaMEKilichopokwenye_KiasiChaChakulaKwaWiki) / 7


# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaCPKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaCPTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaCPKilichopokwenye_KiasiChaChakulaKwaWiki) / 7

# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaFATKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaFATTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaFATKilichopokwenye_KiasiChaChakulaKwaWiki) / 7


# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaCARBOKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaCARBOTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaCARBOKilichopokwenye_KiasiChaChakulaKwaWiki) / 7

# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaCALCKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaCALCTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaCALCKilichopokwenye_KiasiChaChakulaKwaWiki) / 7

# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaPKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaPTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaPKilichopokwenye_KiasiChaChakulaKwaWiki) / 7

# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaLYSINKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaLYSINTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaLYSINKilichopokwenye_KiasiChaChakulaKwaWiki) / 7

# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaMETHKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaMETHTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaMETHKilichopokwenye_KiasiChaChakulaKwaWiki) / 7


# @receiver(pre_save, sender=TaarifaZaKuku)
# def set_KiasiChaTRYPTOKilichopokwenye_KiasiChaChakulaKwaWiki(sender, **kwargs):
#     quryset = kwargs['instance']
#     quryset.KiasiChaTRYPTOTHKilichopokwenye_KiasiChaChakulaKwaSiku = (quryset.KiasiChaTRYPTOKilichopokwenye_KiasiChaChakulaKwaWiki) / 7


#-------------------MWISHO WA MFUGAJI APP--------------------


