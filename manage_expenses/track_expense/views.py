from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from numpy import identity
from .models import *
from .forms import *
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
import datetime

# Create your views here.

@login_required
def home(request):
    total_spent = Expense.objects.filter(user_id = request.user.id)
    income =  total_spent.filter(expense_type = "income")
    expenditure =  total_spent.filter(expense_type = "expenditure")
    total_spent =  total_spent.order_by('date')
    return render(request, 'home.html', locals())

@login_required
def add_expense(request):
    form = Add_Expense(request.POST)
    if request.method == 'POST':
        form = Add_Expense(data = request.POST)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            expense = form.save(commit=False)
            expense.user_id = user
            expense.save()
            messages.success(request, f'Expense added successfully')
            return redirect('home')
    return render(request, 'add_expense.html', locals())

@login_required
def delete_expense(request, pk):
    obj = get_object_or_404(Expense, pk = pk)
    obj.delete()
    messages.warning(request, f'Expense deleted')
    return redirect('home')

@login_required
def edit_expense(request,pk):
    obj = Expense.objects.get(id=pk)
    form = Add_Expense(instance = obj)
    if request.method == 'POST':
        form = Add_Expense(data = request.POST, instance = obj)
        if form.is_valid():
            user = User.objects.get(id=request.user.id)
            expense = form.save(commit=False)
            expense.user_id = user
            expense.save()
            messages.success(request, f'Expense edited successfully')
            return redirect('home')
    return render(request, 'add_expense.html', locals())


# def register(request):
#     if request.method == 'POST':
#         form = User_register(request.POST)
#         if form.is_valid():
#             user = form.save()
#             messages.success(request, f'Your account has been created! You are now able to log in')
#             return redirect('login')
#     else:
#         form = User_register()
#     return render(request, 'register.html', locals())