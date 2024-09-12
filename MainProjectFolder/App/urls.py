from django.urls import path
from . import views

#app_name = "polls"

urlpatterns = [
    
    path('GetAllAdminView/', views.GetAllAdminView.as_view(), name='GetAllAdminView'),
    path('GetAllMyUserView/', views.GetAllMyUserView.as_view(), name='GetAllMyUserView'),
    
    path('GetAllHudumaView/', views.GetAllHudumaView.as_view(), name='GetAllHudumaView'),
    path('GetAinaZaChanjoView/', views.GetAinaZaChanjoView.as_view(), name='GetAinaZaChanjoView'),
    
    path('GetAllVyakulaView/', views.GetAllVyakulaView.as_view(), name='GetAllVyakulaView'),
    path('GetAllVyakulaWangaView/', views.GetAllVyakulaWangaView.as_view(), name='GetAllVyakulaWangaView'),
    path('GetAllVyakulaMadiniNaVitaminiView/', views.GetAllVyakulaMadiniNaVitaminiView.as_view(), name='GetAllVyakulaMadiniNaVitaminiView'),
    path('GetAllVyakulaVimengenyaView/', views.GetAllVyakulaVimengenyaView.as_view(), name='GetAllVyakulaVimengenyaView'),
    

    path('GetIdadiYaKilosView/', views.GetIdadiYaKilosView.as_view(), name='GetIdadiYaKilosView'),    



    path('GetMgawanjoWaHudumaView/', views.GetMgawanjoWaHudumaView.as_view(), name='GetMgawanjoWaHudumaView'),
    path('GetAinaZaKukuView/', views.GetAinaZaKukuView.as_view(), name='GetAinaZaKukuView'),
    path('GetAinaZaNdegeView/', views.GetAinaZaNdegeView.as_view(), name='GetAinaZaNdegeView'),

    path('GetIdadiYaKukuView/', views.GetIdadiYaKukuView.as_view(), name='GetIdadiYaKukuView'),
    path('GetUmriWaKukuView/', views.GetUmriWaKukuView.as_view(), name='GetUmriWaKukuView'),
    path('GetAllSikuView/', views.GetAllSikuView.as_view(), name='GetAllSikuView'),
    path('GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView/', views.GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView.as_view(), name='GetTaarifaZaKukuByCategoryZaAinaYaKukuNaUmriWaKukuView'),

    path('VyakulaCart/', views.VyakulaCartView.as_view(), name='VyakulaCart'),
    path('VyakulaOrder/', views.VyakulaOrderView.as_view(), name='Vyakula--order-list'),
    path('VyakulaDeleteCartItem/', views.VyakulaDeleteCartItemView.as_view(), name='VyakulaDeleteCartItem'),
    path('GetAllVyakulaOrderItemsView/', views.GetAllVyakulaOrderItemsView.as_view(), name='GetAllVyakulaOrderItemsView'),


    path('GetMaktabaYaLisheCategoriesView/', views.GetMaktabaYaLisheCategoriesView.as_view(), name='GetMaktabaYaLisheCategoriesView'),
    path('GetMaktabaYaLisheContentsView/', views.GetMaktabaYaLisheContentsView.as_view(), name='GetMaktabaYaLisheContentsView'),
    
    path('GetMuongozoWaLisheView/', views.GetMuongozoWaLisheView.as_view(), name='GetMuongozoWaLisheView'),
    path('GetMatumiziSahihiYaIndibataView/', views.GetMatumiziSahihiYaIndibataView.as_view(), name='GetMatumiziSahihiYaIndibataView'),
    path('GetJamiiYaMfugajiCategoriesView/', views.GetJamiiYaMfugajiCategoriesView.as_view(), name='GetJamiiYaMfugajiCategoriesView'),
    path('GetJamiiYaMfugajiContentsView/', views.GetJamiiYaMfugajiContentsView.as_view(), name='GetJamiiYaMfugajiContentsView'),


    #---------------KUMBUSHO LA KUSAFISHA BANDA-------------
    path('AddKumbushoUsafishajiBandaView/', views.AddKumbushoUsafishajiBandaView.as_view(), name='AddKumbushoUsafishajiBandaView'),
    path('GetAllKumbushoUsafishajiBandaView/', views.GetAllKumbushoUsafishajiBandaView.as_view(), name='GetAllKumbushoUsafishajiBandaView'),
    #path('DeleteKumbushoUsafishajiBandaByUserItsSelfView/', views.DeleteKumbushoUsafishajiBandaByUserItsSelfView.as_view(), name='DeleteKumbushoUsafishajiBandaByUserItsSelfView'),
    path('DeleteKumbushoUsafishajiBandaByUserItsSelfView/<int:pk>/delete/', views.DeleteKumbushoUsafishajiBandaByUserItsSelfView.as_view(), name='DeleteKumbushoUsafishajiBandaByUserItsSelfView'),

    #----------------KUMBUSHO LA CHANJO------------------
    path('AddKumbushoLaChanjoView/', views.AddKumbushoLaChanjoView.as_view(), name='AddKumbushoLaChanjoView'),
    path('GetAllKumbushoLaChanjoView/', views.GetAllKumbushoLaChanjoView.as_view(), name='GetAllKumbushoLaChanjoView'),
    #path('DeleteKumbushoLaChanjoByUserItsSelfView/', views.DeleteKumbushoLaChanjoByUserItsSelfView.as_view(), name='DeleteKumbushoLaChanjoByUserItsSelfView'),
    path('DeleteKumbushoLaChanjoByUserItsSelfView/<int:pk>/delete/', views.DeleteKumbushoLaChanjoByUserItsSelfView.as_view(), name='DeleteKumbushoLaChanjoByUserItsSelfView'),
   
    #----------------KUMBUSHO LA UATAMIAJI WA MAYAI------------------
    path('AddKumbushoLaUatamiajiWaMayaiView/', views.AddKumbushoLaUatamiajiWaMayaiView.as_view(), name='AddKumbushoLaUatamiajiWaMayaiView'),
    path('GetAllKumbushoLaUatamiajiWaMayaiView/', views.GetAllKumbushoLaUatamiajiWaMayaiView.as_view(), name='GetAllKumbushoLaUatamiajiWaMayaiView'),
    #path('DeleteKumbushoLaUatamiajiWaMayaiByUserItsSelfView/', views.DeleteKumbushoLaUatamiajiWaMayaiByUserItsSelfView.as_view(), name='DeleteKumbushoLaUatamiajiWaMayaiByUserItsSelfView'),
    path('DeleteKumbushoLaUatamiajiWaMayaiByUserItsSelfView/<int:pk>/delete/', views.DeleteKumbushoLaUatamiajiWaMayaiByUserItsSelfView.as_view(), name='DeleteKumbushoLaUatamiajiWaMayaiByUserItsSelfView'),

    #--------KUMBUSHO LA MABADILIKO YA LISHE
    path('AddKumbushoLaMabadilikoYaLisheView/', views.AddKumbushoLaMabadilikoYaLisheView.as_view(), name='AddKumbushoLaMabadilikoYaLisheView'),
    path('GetAllKumbushoLaMabadilikoYaLisheView/', views.GetAllKumbushoLaMabadilikoYaLisheView.as_view(), name='GetAllKumbushoLaMabadilikoYaLisheView'),
    #path('DeleteKumbushoLaMabadilikoYaLisheByUserItsSelfView/', views.DeleteKumbushoLaMabadilikoYaLisheByUserItsSelfView.as_view(), name='DeleteKumbushoLaMabadilikoYaLisheByUserItsSelfView'),
    path('DeleteKumbushoLaMabadilikoYaLisheByUserItsSelfView/<int:pk>/delete/', views.DeleteKumbushoLaMabadilikoYaLisheByUserItsSelfView.as_view(), name='DeleteKumbushoLaMabadilikoYaLisheByUserItsSelfView'),

    #----------------DUKA LAKO------------------
    path('AddDukaLakoView/', views.AddDukaLakoView.as_view(), name='AddDukaLakoView'),
    path('GetAllDukaLakoView/', views.GetAllDukaLakoView.as_view(), name='GetAllDukaLakoView'),
    #path('DeleteKumbushoLaChanjoByUserItsSelfView/', views.DeleteKumbushoLaChanjoByUserItsSelfView.as_view(), name='DeleteKumbushoLaChanjoByUserItsSelfView'),

    path('GetAllDukaLakeByClickingPostedProductView/', views.GetAllDukaLakeByClickingPostedProductView.as_view(), name='GetAllDukaLakeByClickingPostedProductView'),
    path('GetAllDukaLakoPostedByUserItselfView/', views.GetAllDukaLakoPostedByUserItselfView.as_view(), name='GetAllDukaLakoPostedByUserItselfView'),

    path('RetrieveDukaLakoPostView/<int:pk>/', views.RetrieveDukaLakoPostView.as_view(), name='RetrieveDukaLakoPostView'),
    path('UpdateDukaLakoPostView/<int:pk>/edit/', views.UpdateDukaLakoPostView.as_view(), name='UpdateDukaLakoPostView'),
    path('DeleteDukaLakoPostView/<int:pk>/delete/', views.DeleteDukaLakoPostView.as_view(), name='DeleteDukaLakoPostView'),

    path('ToggleLikeView/<int:pk>/', views.ToggleLikeView.as_view(), name='ToggleLikeView'),
    path('AddMaoniView/', views.AddMaoniView.as_view(), name='AddMaoniView'),
    path('CheckLikeStatus/<int:pk>/', views.CheckLikeStatus.as_view(), name='CheckLikeStatus'),


    path('GetConstantFoodKilosForEachItemView/', views.GetConstantFoodKilosForEachItemView.as_view(), name='GetConstantFoodKilosForEachItemView'),
        
    path('notifications/', views.NotificationListView.as_view(), name='notification-list'),
    path('CountUnseenNotificationsView/', views.CountUnseenNotificationsView.as_view(), name='CountUnseenNotificationsView'),
    path('MarkNotificationsAsSeenView/', views.MarkNotificationsAsSeenView.as_view(), name='MarkNotificationsAsSeenView'),



]
