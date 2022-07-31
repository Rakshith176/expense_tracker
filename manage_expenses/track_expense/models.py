from django.db import models
from django.contrib.auth.models import User
from user.models import User

# Create your models here.

expense_type=(
  ('income','Income'),
  ('expenditure','Expenditure'),
)

class Expense(models.Model):
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    expense_type =  models.CharField(choices =expense_type,default = 'expenditure',max_length = 15)
    amount = models.IntegerField()
    date = models.DateField()
    description = models.CharField(max_length=100)

    def __str__(self):
      return self.description

# class User(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE)
#     profession = models.CharField(max_length=15)
#     dob = models.DateField()

#     def __str__(self):
#       return self.user.username