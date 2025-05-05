from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def home(request):
    message = {
        'type': 'success',  # could be 'success', 'warning', or 'error'
        'title': 'Welcome Back!',
        'text': 'You have successfully logged in.'
    }
    return render(request, 'templates_app/home.html', {
        'user_name': 'Giorgi',
        'is_admin': True,
        'message': message
    })

@login_required
def about(request):
    return render(request, 'templates_app/about.html')

@login_required
def posts(request):
    sample_posts = [
        {'title': 'First Post', 'date': '2025-04-01'},
        {'title': 'Second Post', 'date': '2025-04-15'},
    ]
    return render(request, 'templates_app/posts.html', {'posts': sample_posts})

from .models import Profile

@login_required
def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'templates_app/profiles.html', {'profiles': profiles})



from .forms import ContactForm, EmployeeModelForm
from .models import Contact, Employee

@login_required
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            Contact.objects.create(
                name=form.cleaned_data['name'],
                email=form.cleaned_data['email'],
                message=form.cleaned_data['message']
            )
            return redirect("templates_app:contact")
            
        else:
            contacts = Contact.objects.all().order_by('-created_at')  
            return render(request, "templates_app/contact_form.html", {
                "form": form,
                "contacts": contacts
            })
    else:
        form = ContactForm()
        contacts = Contact.objects.all().order_by('-created_at')
        return render(request, "templates_app/contact_form.html", {
            "form": form,
            "contacts": contacts
        })

    
@login_required
def employee(request):
    if request.method == "POST":
        form = EmployeeModelForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("templates_app:employee")
    else:
        form = EmployeeModelForm()
        employees = Employee.objects.all()
        context = {
            "form": form,
            "employees": employees,
        }

        return render(request, "templates_app\employee_model_form.html", context)
    

@login_required
def edit_emp(request, pk):
    employee = Employee.objects.get(id=pk)
    if request.method == "POST":
        form = EmployeeModelForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, "Employee updated successfully.")
            return redirect("templates_app:employee")
    else:
        form = EmployeeModelForm(instance=employee)
        employees = Employee.objects.all()
        context = {
            "form": form,
            "employee": employee,
            "employees": employees
        }
        
        return render(request, "templates_app\edit_employee.html", context)
    
# # while using forms.Form instead of ModelForm
# @login_required
# def edit_emp(request, pk):
#     employee = get_object_or_404(Employee, id=pk)

#     if request.method == "POST":
#         form = EmployeeForm(request.POST)
#         if form.is_valid():
#             # Update fields manually
#             employee.first_name = form.cleaned_data['first_name']
#             employee.last_name = form.cleaned_data['last_name']
#             employee.email = form.cleaned_data['email']
#             employee.position = form.cleaned_data['position']
#             employee.save()

#             messages.success(request, "Employee updated successfully.")
#             return redirect("templates_app:employee")
#     else:
#         # Populate the form with existing data
#         form = EmployeeForm(initial={
#             'first_name': employee.first_name,
#             'last_name': employee.last_name,
#             'email': employee.email,
#             'position': employee.position,
#         })

#     employees = Employee.objects.all()
#     context = {
#         "form": form,
#         "employee": employee,
#         "employees": employees
#     }
#     return render(request, "templates_app/edit_employee.html", context)


@login_required
def delete_emp(request, pk):
    employee = Employee.objects.get(id=pk)
    employee.delete()
    messages.success(request, "Employee Deleted Successfully.")
    return redirect("templates_app:employee")
    
    

