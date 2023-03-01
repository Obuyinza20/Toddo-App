from django.urls import path
from  .views import TaskList, TaskDetail, TaskCreate, UpdateView, DeleteTask, loginPage, registerPage
from .f_views import F_updateTask, signUp
from django.contrib.auth.views import LogoutView


urlpatterns=[
    path('login-page/' , loginPage.as_view(), name='login'),
     path('sign-up/' , registerPage.as_view(), name = 'signup' ),
     path('logged-out/' , LogoutView.as_view(next_page = 'login'), name='logout'),
    path('', TaskList.as_view(), name = 'tasks'),
    path('task/<int:pk>/' ,TaskDetail.as_view(), name = 'taskdetail' ), #by default , the detail view looks for a pk unique key
    path('create-task/' , TaskCreate.as_view(), name='createtask'),
    path('update-task/<int:pk>/' ,F_updateTask, name = 'updatetask' ),
    path('delete-task/<int:pk>/' ,DeleteTask.as_view(), name = 'deletetask' )
]