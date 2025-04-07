from django.urls import path
from Frontend import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('coursepage/<int:Cid>/', views.coursepage, name='coursepage'),
    path('admissionpage/', views.admissionpage, name='admissionpage'),
    path('saveadmission/', views.saveadmission, name='saveadmission'),
    path('savecontact/', views.savecontact, name='savecontact'),

]