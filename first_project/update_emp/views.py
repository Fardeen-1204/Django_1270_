from django.shortcuts import render
from first_app.models import EmpDetails

# Create your views here.
def update_emp_page(request,pk):
    pr=pk
    data = EmpDetails.objects.get(id=pk)
    context = {'emp_name': data.emp_name,
               'emp_city': data.emp_city,
               'emp_company': data.emp_company,
               'pr':data.id}
    return render(request,"update_emp.html",context)

def update_emp(request,pk):
    data=EmpDetails.objects.get(id=pk)
    context={'emp_name':data.emp_name,
             'emp_city':data.emp_city,
             'emp_company':data.emp_company,
             'pr': data.id,
             'msg':'UPDATED'}
    msg='not updated'
    if request.method=='POST':
        data.emp_name=request.POST['up_Empname']
        data.emp_city=request.POST['up_Empcity']
        data.emp_company=request.POST['up_Empcompany']
        data.save()

        msg="updated"
    return render(request,"update_emp.html",context)

