from django.contrib import admin
from App.models import *
# Register your models here.
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from import_export.admin import ImportExportModelAdmin

class MyUserAdmin(BaseUserAdmin):
    list_display=('username', 'email', 'phone', 'date_joined', 'last_login', 'is_admin', 'is_active')
    search_fields=('email', 'first_name', 'last_name')
    readonly_fields=('date_joined', 'last_login')
    filter_horizontal=()
    list_filter=('last_login',)
    fieldsets=()

    add_fieldsets=(
        (None,{
            'classes':('wide'),
            'fields':('email', 'username','phone', 'first_name', 'middle_name', 'last_name', 'company_name', 'phone', 'password1', 'password2'),
        }),
    )

    ordering=('email',)


@admin.register(Huduma)
class HudumaAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaLaHuduma","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaLaHuduma"]

@admin.register(MgawanjoWaHuduma)
class MgawanjoWaHudumaAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaLaHuduma","Category","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaLaHuduma"]


@admin.register(IdadiYaKuku)
class IdadiYaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id","IdadiYaKuku","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["IdadiYaKuku"]


@admin.register(UmriWaKuku)
class UmriWaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id","UmriKwaWiki","UmriKwaSiku","Created","Updated"]
    list_filter =["Created","Updated","UmriKwaWiki"]
    search_fields = ["UmriKwaWiki","UmriKwaSiku"]


@admin.register(AinaZaKuku)
class AinaZaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id","AinaYaKuku","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["AinaYaKuku"]


@admin.register(AinaZaNdege)
class AinaZaNdegeAdmin(ImportExportModelAdmin):
    list_display = ["id","AinaYaNdege","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["AinaYaNdege"]

@admin.register(MakundiYaVyakula)
class MakundiYaVyakulaAdmin(ImportExportModelAdmin):
    list_display = ["id","Jina","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Jina"]

@admin.register(VipindiVyaKuku)
class VipindiVyaKukuAdmin(ImportExportModelAdmin):
    list_display = ["id","Kipindi","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Kipindi"]


@admin.register(UserStatus)
class UserStatusAdmin(ImportExportModelAdmin):
    list_display = ["id","Status","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Status"]

@admin.register(UserRole)
class UserRoleAdmin(ImportExportModelAdmin):
    list_display = ["id","Role","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Role"]


@admin.register(AinaZaChanjo)
class AinaZaChanjoAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaLaChanjo","Kutolewa","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaLaChanjo"]


@admin.register(KumbushoLaUatamiajiWaMayai)
class KumbushoLaUatamiajiWaMayaiAdmin(ImportExportModelAdmin):
    list_display = ["id","username","phone","time_left","is_red","KiasiChaMayai","SikuYaNgapiTokaKuatamiwa","JinaLaUlipoYatoaMayai","NambaYakeYaSimu", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["username"]


@admin.register(DukaLako)
class DukaLakoAdmin(ImportExportModelAdmin):
    list_display = ["id","username","phone","Title","Status","Maelezo", "Created","Updated"]
    list_filter =["Status", "Created","Updated"]
    search_fields = ["username", "phone","Title"]


@admin.register(Maoni)
class MaoniAdmin(ImportExportModelAdmin):
    list_display = ["id","username","phone","Maoni", "Created","Updated"]
    list_filter =["Maoni", "Created","Updated"]
    search_fields = ["username", "phone","Maoni"]



@admin.register(KumbushoLaChanjo)
class KumbushoLaChanjoAdmin(ImportExportModelAdmin):
    list_display = ["id","username","phone","time_left","is_red", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["username"]


@admin.register(KumbushoLaMabadilikoYaLishe)
class KumbushoLaMabadilikoYaLisheAdmin(ImportExportModelAdmin):
    list_display = ["id","username","phone","LengoLaKufuga","KundiLaKukuWake","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["username"]



@admin.register(OTP)
class OTPAdmin(ImportExportModelAdmin):
    list_display = ["id","user","otp", "created_at"]
    list_filter =["created_at"]
    search_fields = ["user"]





@admin.register(MudaWaKumbushoUsafishajiBanda)
class MudaWaKumbushoUsafishajiBandaAdmin(ImportExportModelAdmin):
    list_display = ["id","Muda","StartingTime","EndingTime"]
    list_filter =["StartingTime","EndingTime"]
    search_fields = ["Muda"]


@admin.register(KumbushoUsafishajiBanda)
class KumbushoUsafishajiBandaAdmin(ImportExportModelAdmin):
    list_display = ["id","username","phone","email","Muda","Awamu","Location","time_left","is_red","Created","Updated"]
    list_filter =["Awamu"]
    search_fields = ["username"]


@admin.register(LevelZaWafugaji)
class LevelZaWafugajiAdmin(ImportExportModelAdmin):
    list_display = ["id","Level","Nyota","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Level"]


@admin.register(Mikoa)
class MikoaAdmin(ImportExportModelAdmin):
    list_display = ["id","JinaLaMkoa","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["JinaLaMkoa"]

@admin.register(IdadiYaKilos)
class IdadiYaKilosAdmin(ImportExportModelAdmin):
    list_display = ["id","IdadiYaKilos","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["IdadiYaKilos"]


@admin.register(Siku)
class SikuAdmin(ImportExportModelAdmin):
    list_display = ["id","Siku","Wiki", "Mwezi", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Siku"]



@admin.register(MaktabaYaLisheCategories)
class MaktabaYaLisheCategoriesAdmin(ImportExportModelAdmin):
    list_display = ["id","CategoryName","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]


@admin.register(MaktabaYaLisheContents)
class MaktabaYaLisheContentsAdmin(ImportExportModelAdmin):
    list_display = ["id","Title","CategoryName","Created","Updated"]
    list_filter =["Created","Updated", "CategoryName"]
    search_fields = ["Title"]

@admin.register(MuongozoWaLishe)
class MuongozoWaLisheAdmin(ImportExportModelAdmin):
    list_display = ["id","Title","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Title"]


@admin.register(MatumiziSahihiYaIndibata)
class MatumiziSahihiYaIndibataAdmin(ImportExportModelAdmin):
    list_display = ["id","Title","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Title"]



@admin.register(JamiiYaMfugajiCategories)
class JamiiYaMfugajiCategoriesAdmin(ImportExportModelAdmin):
    list_display = ["id","CategoryName","Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["CategoryName"]




@admin.register(JamiiYaMfugajiContents)
class JamiiYaMfugajiContentsAdmin(ImportExportModelAdmin):
    list_display = ["id","FullName","Location","CategoryName","Title","Created","Updated"]
    list_filter =["Created","Updated","CategoryName","Location"]
    search_fields = ["FullName"]


@admin.register(UnitZaVyakula)
class UnitZaVyakulaAdmin(ImportExportModelAdmin):
    list_display = ["id", "Unit", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["Unit"]

@admin.register(Notification)
class NotificationAdmin(ImportExportModelAdmin):
    list_display = ["id","username","PostOwner","duka_lako", "created_at"]
    list_filter =["created_at","duka_lako"]
    search_fields = ["username"]


@admin.register(Vyakula)
class VyakulaAdmin(ImportExportModelAdmin):
    list_display = [
    "id",
    "product_name",
    "TotalPercentageRequired_Starter",
    "TotalPercentageRequired_Grower",
    "TotalPercentageRequired_Layer",
    "TotalPercentageRequired_Finisher",
    "price",
    "ProductQuantity",
    "Created",
    "Updated"
    ]
    list_filter =["Created","Updated"]
    search_fields = ["product_name"]




#---------------------Products  CART---------------------
class VyakulaCartAdmin(admin.ModelAdmin):
    list_display = ["id","user","ordered", "total_price","total_Kilos", "Created","Updated"]
    list_filter =["Created"]
    search_fields = ["user"]

class VyakulaCartItemsAdmin(admin.ModelAdmin):
    list_display = ["id","user","cart", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]


@admin.register(VyakulaOrder)  
class VyakulaOrderAdmin(ImportExportModelAdmin):
    list_display = ["id","TotalFoodMixerPercentage","Customer","total_price", "created"]
    list_filter =["created"]
    search_fields = ["Customer"]

@admin.register(VyakulaOrderItems)
class VyakulaOrderItemsAdmin(ImportExportModelAdmin):
    list_display = ["id","user","order", "product","price","quantity", "Created","Updated"]
    list_filter =["Created","Updated"]
    search_fields = ["user"]



@admin.register(TaarifaZaKuku)
class TaarifaZaKukuAdmin(ImportExportModelAdmin):
    list_display = [
    "id", 
    "AinaYaKuku",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_1_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_2_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_3_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_4_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_5_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_6_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_7_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_8_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_9_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_10_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_11_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_12_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_13_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_14_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_15_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_16_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_17_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_18_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_19_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_20_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_21_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_22_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_23_KwaWiki",
    "KiasiChaChakulaKwaKukuWaUmriWaWiki_24_KwaWiki",
    "Created",
    "Updated"
    ]
    list_filter =["Created","Updated"]
    # search_fields = ["Unit"]












@admin.register(EmailSendCount_KumbushoLaUatamiajiWaMayai)
class EmailSendCount_KumbushoLaUatamiajiWaMayaiAdmin(ImportExportModelAdmin):
    list_display = ["id", "username", "count","last_sent"]
    list_filter =["last_sent"]
    search_fields = ["username"]


@admin.register(EmailSendCount_KumbushoUsafishajiBanda)
class EmailSendCount_KumbushoUsafishajiBandaAdmin(ImportExportModelAdmin):
    list_display = ["id", "username", "count","last_sent"]
    list_filter =["last_sent"]
    search_fields = ["username"]



    



#----------------MWISHO WA BASA KUKU-----------------------------


admin.site.register(MyUser, MyUserAdmin)

admin.site.register(VyakulaCart, VyakulaCartAdmin)
admin.site.register(VyakulaCartItems, VyakulaCartItemsAdmin)


