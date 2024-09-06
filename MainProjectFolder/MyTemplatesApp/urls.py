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
     
]