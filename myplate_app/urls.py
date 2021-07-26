from django.contrib import admin
from . import views
from django.urls import path,include
from django.views.generic.base import TemplateView

app_name='myplate_app'

urlpatterns = [
    path('myplate_app_list/', views.FoodListView.as_view(), name='list'),   #url for FoodList View
    path('set_goal/', views.GoalCreateView.as_view(), name='set_goal'),
    path('checkout/', views.CheckOutView.as_view(), name='checkout'),
    path('previous_records/', views.PreRecordsView.as_view(), name='pre_records'),
    path('save_rec/', views.save_records, name= 'save_rec'),      #since its a function based view, so url is different compared to others

]