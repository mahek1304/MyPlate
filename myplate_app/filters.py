import django_filters
from django_filters import CharFilter
from .models import FoodItems

#Filter created for searching the food items based on their name
class FoodFilter(django_filters.FilterSet):
    food_name = CharFilter(field_name = 'name', lookup_expr = 'icontains', label = 'Search Food Items') #lookupup_expr is used to find 
                                                                                                        #the food item and label is used 
                                                                                                        #for the front end part

    class Meta :
        model = FoodItems
        fields = ('food_name',)