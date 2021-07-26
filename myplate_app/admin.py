from django.contrib import admin
from .models import FoodItems, PreviousRecords, SetGoal

# Register your models here.
class PreRecAdmin(admin.ModelAdmin):    #PreRecAdmin class is made just for displaying the date, since it is a field which cant be modified, so it is necessary to make it readonly
    readonly_fields = ('date',)

admin.site.register(FoodItems)
admin.site.register(SetGoal)
admin.site.register(PreviousRecords, PreRecAdmin)   #PreRecAdmin is added here since the date is a part of PreviousRecords View