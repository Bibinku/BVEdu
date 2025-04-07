from django.urls import path
from BVapp import views
urlpatterns=[
   path('indexpage/',views.indexpage,name='indexpage'),
   path('addcourse/',views.addcourse,name='addcourse'),
   path('savecourse/',views.savecourse,name='savecourse'),
   path('displaycourse/',views.displaycourse,name='displaycourse'),
   path('updatecousre/<int:Uid>/', views.updatecousre, name="updatecousre"),
   path('editcourse/<int:Cid>/', views.editcourse, name="editcourse"),
   path('deletecourse/<int:Delid>/', views.deletecourse, name="deletecourse"),
   path('adminlogin/',views.adminlogin,name='adminlogin'),
   path('admin/', views.admin, name="admin"),
   path('adminlogout/', views.adminlogout, name="adminlogout"),
   path('displayadmission/', views.displayadmission, name="displayadmission"),
   path('deleteadmission/<int:Aid>/', views.deleteadmission, name="deleteadmission"),
   path('displaycontact/', views.displaycontact, name="displaycontact"),
   path('deletecontact/<int:Cid>/', views.deletecontact, name="deletecontact"),
]