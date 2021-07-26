from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView,TemplateView
from .models import FoodItems, PreviousRecords, SetGoal
from django.urls import reverse_lazy, reverse
from .filters import FoodFilter

#View for FoodItems Model
class FoodListView(ListView):
    model = FoodItems
    template_name = 'myplate_app/list.html'

    #for the working of search field ie for filtering the food items
    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context['filter'] = FoodFilter(self.request.GET, queryset = self.get_queryset())
        return context

#View for the user to enter goal
class GoalCreateView(CreateView):
    model = SetGoal
    fields = ['goal',]
    success_url = reverse_lazy('myplate_app:list')

#View for the checkout page
class CheckOutView(TemplateView):
    template_name = 'myplate_app/checkout.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['goal'] = SetGoal.objects.values().last().get("goal")   #creates a dict with key value pair, where id and goal are the keys. The last() method is used to retrieve the last value. get() method retrives the value of the key 'goal'
        return context

#View for the save records page
def save_records(request):
     
    if request.method == "POST":
        user = request.POST.get('user','')
        goal = request.POST.get('goal_set','')          #'goal_set' is the same name as that used in models for declaring the fields
        calories = request.POST.get('totalCalories','')

        previous_records = PreviousRecords(user=user, goal_set=goal, totalCalories=calories)    #Stores the values from the PreviousRecords model for each field resp.
        previous_records.save()
        return redirect('../previous_records')          #While using redirect, we need to give the url
    return render(request,'myplate_app/save_rec.html')  #aAnd while using render, we need to give the '.html'


class PreRecordsView(ListView):
    model = PreviousRecords
    template_name = 'myplate_app/previous_records.html'
    context_object_name = 'records'
    ordering = ['date']

    def get_queryset(self):
        filter_list = PreviousRecords.objects.filter(user = self.request.user.first_name + ' ' + self.request.user.last_name)
        return filter_list.order_by('-date')[:10]


        #return PreviousRecords.objects.filter(user = self.request.user.first_name + ' ' + self.request.user.last_name)






    
