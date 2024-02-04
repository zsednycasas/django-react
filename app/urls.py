from django.urls import path
from . import views

# POST API URLs
urlpatterns = [

#CREATE API
path('create-student/', views.CreateStudent, name='create_student'),
#READ API
path('get-all-students/', views.GetAllStudents, name='get_all_students'),
    
#UPDATE API
path('edit-student/<int:pk>/', views.EditStudent, name='edit_student'),

#DELETE API
path('delete-student/<int:pk>/', views.DeleteStudent, name='delete_student'),

]
