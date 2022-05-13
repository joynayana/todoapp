from django.urls import path
from . import views

urlpatterns = [
    path('',views.task_view,name='task_view'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('gtasklist/',views.TaskListView.as_view(),name='gtasklist')

]
