from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import EmployeeRegistrationForm, GasSaleForm
from .models import GasSale

def register_employee(request):
    if request.method == "POST":
        form = EmployeeRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # Redirect to homepage after registration
    else:
        form = EmployeeRegistrationForm()
    return render(request, 'register_employee.html', {'form': form})

@login_required
def record_sale(request):
    if request.method == "POST":
        form = GasSaleForm(request.POST)
        if form.is_valid():
            sale = form.save(commit=False)
            sale.employee = request.user.employee  # Assign logged-in employee
            sale.save()
            return redirect('home')  # Redirect after saving
    else:
        form = GasSaleForm()
    return render(request, 'record_sale.html', {'form': form})

@login_required
def sales_report(request):
    sales = GasSale.objects.all()
    return render(request, 'sales_report.html', {'sales': sales})
