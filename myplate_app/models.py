from django.db import models
from django.contrib.auth.models import User

from django.db.models.deletion import CASCADE

# Model for Food Details
class FoodItems(models.Model):
    name = models.CharField(max_length = 100, unique = True)
    calorie = models.DecimalField(max_digits = 10, decimal_places = 2)
    image = models.ImageField(upload_to = 'images', null = True)

    def str(self):
        return self.name

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'FoodItems'

#Model for user's goal of calories
class SetGoal(models.Model):
    goal = models.DecimalField(max_digits = 10, decimal_places = 2)

    def str(self):
        return self.goal

#This model is created to display the previous records of a particular user. All the below mentioned fields will be hidden.
class PreviousRecords(models.Model):
    user = models.CharField(max_length=100)
    date = models.DateField(auto_now= True )
    totalCalories = models.DecimalField(max_digits = 10, decimal_places = 2)
    goal_set =  models.DecimalField(max_digits = 10, decimal_places = 2)

    def str(self):
        return self.user




