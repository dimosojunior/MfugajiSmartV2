from . import views
from django.urls import path


urlpatterns = [
	

    

    #---------------KWA AJILI YA APIS --------------
    #path('', views.home, name='home'),
    path('', views.Mylogin_user, name='Mylogin_user'),
    path('Mylogout_user/', views.Mylogout_user, name='Mylogout_user'),
    #path('register/', views.create_user, name='register'),
    path('MyUserRegistrationView/', views.MyUserRegistrationView, name='MyUserRegistrationView'),



    path('AllKumbushoLaChanjo/', views.AllKumbushoLaChanjo, name='AllKumbushoLaChanjo'),
    path('search_KumbushoLaChanjo_autocomplete/', views.search_KumbushoLaChanjo_autocomplete, name='search_KumbushoLaChanjo_autocomplete'),
    path('AllKumbushoLaChanjo_ISRED/', views.AllKumbushoLaChanjo_ISRED, name='AllKumbushoLaChanjo_ISRED'),
    path('Tuma_KumbushoLaChanjo_Kwa_Wote/', views.Tuma_KumbushoLaChanjo_Kwa_Wote, name='Tuma_KumbushoLaChanjo_Kwa_Wote'),
    path('deleteKumbushoLaChanjo/<int:id>/', views.deleteKumbushoLaChanjo, name='deleteKumbushoLaChanjo'),
    path('All_EmailSendCount_KumbushoLaChanjo/', views.All_EmailSendCount_KumbushoLaChanjo, name='All_EmailSendCount_KumbushoLaChanjo'),
    path('search_EmailSendCount_KumbushoLaChanjo_autocomplete/', views.search_EmailSendCount_KumbushoLaChanjo_autocomplete, name='search_EmailSendCount_KumbushoLaChanjo_autocomplete'),



    #-------------KUMBUSHO LA KUSAFISHA BANDA-------------
    path('AllKumbushoUsafishajiBanda/', views.AllKumbushoUsafishajiBanda, name='AllKumbushoUsafishajiBanda'),
    path('search_KumbushoUsafishajiBanda_autocomplete/', views.search_KumbushoUsafishajiBanda_autocomplete, name='search_KumbushoUsafishajiBanda_autocomplete'),
    path('AllKumbushoUsafishajiBanda_ISRED/', views.AllKumbushoUsafishajiBanda_ISRED, name='AllKumbushoUsafishajiBanda_ISRED'),
    path('Tuma_KumbushoUsafishajiBanda_Kwa_Wote/', views.Tuma_KumbushoUsafishajiBanda_Kwa_Wote, name='Tuma_KumbushoUsafishajiBanda_Kwa_Wote'),
    path('deleteKumbushoUsafishajiBanda/<int:id>/', views.deleteKumbushoUsafishajiBanda, name='deleteKumbushoUsafishajiBanda'),
    path('All_EmailSendCount_KumbushoUsafishajiBanda/', views.All_EmailSendCount_KumbushoUsafishajiBanda, name='All_EmailSendCount_KumbushoUsafishajiBanda'),
    path('search_EmailSendCount_KumbushoUsafishajiBanda_autocomplete/', views.search_EmailSendCount_KumbushoUsafishajiBanda_autocomplete, name='search_EmailSendCount_KumbushoUsafishajiBanda_autocomplete'),
    


    #---------------KUMBUSHO LA UATAMIAJI WA MAYAI-----------
    path('AllKumbushoLaUatamiajiWaMayai/', views.AllKumbushoLaUatamiajiWaMayai, name='AllKumbushoLaUatamiajiWaMayai'),
    path('search_KumbushoLaUatamiajiWaMayai_autocomplete/', views.search_KumbushoLaUatamiajiWaMayai_autocomplete, name='search_KumbushoLaUatamiajiWaMayai_autocomplete'),
    path('AllKumbushoLaUatamiajiWaMayai_ISRED/', views.AllKumbushoLaUatamiajiWaMayai_ISRED, name='AllKumbushoLaUatamiajiWaMayai_ISRED'),
    path('Tuma_KumbushoLaUatamiajiWaMayai_Kwa_Wote/', views.Tuma_KumbushoLaUatamiajiWaMayai_Kwa_Wote, name='Tuma_KumbushoLaUatamiajiWaMayai_Kwa_Wote'),
    path('deleteKumbushoLaUatamiajiWaMayai/<int:id>/', views.deleteKumbushoLaUatamiajiWaMayai, name='deleteKumbushoLaUatamiajiWaMayai'),
    path('All_EmailSendCount_KumbushoLaUatamiajiWaMayai/', views.All_EmailSendCount_KumbushoLaUatamiajiWaMayai, name='All_EmailSendCount_KumbushoLaUatamiajiWaMayai'),
    path('search_EmailSendCount_KumbushoLaUatamiajiWaMayai_autocomplete/', views.search_EmailSendCount_KumbushoLaUatamiajiWaMayai_autocomplete, name='search_EmailSendCount_KumbushoLaUatamiajiWaMayai_autocomplete'),
     







    #---------------------KUMBUSHO LA MABADILIKO YA LISHE---------
    path('AllKumbushoLaMabadilikoYaLishe/', views.AllKumbushoLaMabadilikoYaLishe, name='AllKumbushoLaMabadilikoYaLishe'),
    path('search_KumbushoLaMabadilikoYaLishe_autocomplete/', views.search_KumbushoLaMabadilikoYaLishe_autocomplete, name='search_KumbushoLaMabadilikoYaLishe_autocomplete'),
    path('AllKumbushoLaMabadilikoYaLishe_ISRED/', views.AllKumbushoLaMabadilikoYaLishe_ISRED, name='AllKumbushoLaMabadilikoYaLishe_ISRED'),
    path('Tuma_KumbushoLaMabadilikoYaLishe_Kwa_Wote/', views.Tuma_KumbushoLaMabadilikoYaLishe_Kwa_Wote, name='Tuma_KumbushoLaMabadilikoYaLishe_Kwa_Wote'),
    path('deleteKumbushoLaMabadilikoYaLishe/<int:id>/', views.deleteKumbushoLaMabadilikoYaLishe, name='deleteKumbushoLaMabadilikoYaLishe'),
    path('All_EmailSendCount_KumbushoLaMabadilikoYaLishe/', views.All_EmailSendCount_KumbushoLaMabadilikoYaLishe, name='All_EmailSendCount_KumbushoLaMabadilikoYaLishe'),
    path('search_EmailSendCount_KumbushoLaMabadilikoYaLishe_autocomplete/', views.search_EmailSendCount_KumbushoLaMabadilikoYaLishe_autocomplete, name='search_EmailSendCount_KumbushoLaMabadilikoYaLishe_autocomplete'),






    #------------------------DUKA LAKO-------------------
    path('AllDukaLako/', views.AllDukaLako, name='AllDukaLako'),
    path('search_DukaLako_autocomplete/', views.search_DukaLako_autocomplete, name='search_DukaLako_autocomplete'),
    path('deleteDukaLako/<int:id>/', views.deleteDukaLako, name='deleteDukaLako'),
    path('All_EmailSendCount_DukaLako/', views.All_EmailSendCount_DukaLako, name='All_EmailSendCount_DukaLako'),
    path('search_EmailSendCount_DukaLako_autocomplete/', views.search_EmailSendCount_DukaLako_autocomplete, name='search_EmailSendCount_DukaLako_autocomplete'),
    path('DukaLakoDetailPage/<int:id>/', views.DukaLakoDetailPage, name='DukaLakoDetailPage'),
    path('AllPendingPostiDukaLako/', views.AllPendingPostiDukaLako, name='AllPendingPostiDukaLako'),
    path('HakikiDukaLako/<int:id>/', views.HakikiDukaLako, name='HakikiDukaLako'),








    #--------------------MY USER----------------
    path('AllMyUser/', views.AllMyUser, name='AllMyUser'),
    path('search_MyUser_autocomplete/', views.search_MyUser_autocomplete, name='search_MyUser_autocomplete'),
    path('deleteMyUser/<int:id>/', views.deleteMyUser, name='deleteMyUser'),
    path('All_EmailSendCount_MyUser/', views.All_EmailSendCount_MyUser, name='All_EmailSendCount_MyUser'),
    path('search_EmailSendCount_MyUser_autocomplete/', views.search_EmailSendCount_MyUser_autocomplete, name='search_EmailSendCount_MyUser_autocomplete'),
    path('MyUserDetailPage/<int:id>/', views.MyUserDetailPage, name='MyUserDetailPage'),
    path('AllPendingMyUser/', views.AllPendingMyUser, name='AllPendingMyUser'),
    path('HakikiMyUser/<int:id>/', views.HakikiMyUser, name='HakikiMyUser'),






    #----------------------MAONI---------------
    path('AllMaoni/', views.AllMaoni, name='AllMaoni'),
    path('search_Maoni_autocomplete/', views.search_Maoni_autocomplete, name='search_Maoni_autocomplete'),
    path('deleteMaoni/<int:id>/', views.deleteMaoni, name='deleteMaoni'),
    path('All_EmailSendCount_Maoni/', views.All_EmailSendCount_Maoni, name='All_EmailSendCount_Maoni'),
    path('search_EmailSendCount_Maoni_autocomplete/', views.search_EmailSendCount_Maoni_autocomplete, name='search_EmailSendCount_Maoni_autocomplete'),
    path('MaoniDetailPage/<int:id>/', views.MaoniDetailPage, name='MaoniDetailPage'),
    path('AllPendingMaoni/', views.AllPendingMaoni, name='AllPendingMaoni'),
    path('HakikiMaoni/<int:id>/', views.HakikiMaoni, name='HakikiMaoni'),






    #--------------------WANUNUZI------------------------
    path('AllMikoa/', views.AllMikoa, name='AllMikoa'),
    path('search_Mikoa_autocomplete/', views.search_Mikoa_autocomplete, name='search_Mikoa_autocomplete'),
    #path('AllWanunuzi/', views.AllWanunuzi, name='AllWanunuzi'),
    path('AllWanunuzi/<int:id>/', views.AllWanunuzi, name='AllWanunuzi'),
    path('search_Wanunuzi_username_autocomplete/', views.search_Wanunuzi_username_autocomplete, name='search_Wanunuzi_username_autocomplete'),
    path('search_Wanunuzi_wilaya_autocomplete/', views.search_Wanunuzi_wilaya_autocomplete, name='search_Wanunuzi_wilaya_autocomplete'),
    path('Tuma_Wanunuzi_Kwa_Wote/', views.Tuma_Wanunuzi_Kwa_Wote, name='Tuma_Wanunuzi_Kwa_Wote'),










]