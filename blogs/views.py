from django.shortcuts import redirect, render
from blogs.models import Details
from .forms import detailsform

# Create your views here.

def index(request):
    return render(request, 'blogs/index.html' )

def create(request):
    if request.method=="POST":
        name=request.POST['name']
        age=request.POST['age']
        address=request.POST['address']
        obj=Details.objects.create(name=name,age=age,address=address)
        obj.save()
        return redirect('/')

def retrieve(request):
    details=Details.objects.all()
    return render(request,'blogs/retrieve.html',{'details':details})

def edit(request,id):
    object=Details.objects.get(id=id)
    return render(request,'blogs/edit.html',{'object':object})
    
def update(request,id):
    object=Details.objects.get(id=id)
    form=detailsform(request.POST,instance=object)
    if form.is_valid:
        form.save()
        object=Details.objects.all()
        return redirect('retrieve')

def delete(request,pk):   
        Details.objects.filter(id=pk).delete()
        return redirect('retrieve')