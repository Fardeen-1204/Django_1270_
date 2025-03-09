from django.shortcuts import render,HttpResponse
from .models import EmpDetails
# Create your views here.
def emp_details(request):
    data=EmpDetails.objects.all()
    context={'details':data}
    return render(request,'Emp_details.html',context)
def emp_details_home(request):
    return render(request, "EmpDetails_form.html")
def create_emp_details(request):
    mesg="NOT Saved"
    if request.method=="POST":
        emp_name_form=request.POST['Empname']
        emp_city_form = request.POST['Empcity']
        emp_company_form = request.POST['Empcompany']
        EmpDetails(emp_name=emp_name_form,
                    emp_city=emp_city_form,
                    emp_company=emp_company_form).save()
        mesg="Saved"
    context={'mesg':mesg}
    return render(request,"EmpDetails_form.html",context)

def delete_emp_details(request,pk):
    data=EmpDetails.objects.get(id=pk)
    data.delete()
    details=EmpDetails.objects.all()

    context={'details':details}
    return render(request,"Emp_details.html",context)



# def update_process(request):
#     data = EmpDetails.objects.get(id=pk)
#     msg="not saved"
#
#         msg="saved"
#         context={"msg":msg}
#     return render(request,"update_details.html",context)